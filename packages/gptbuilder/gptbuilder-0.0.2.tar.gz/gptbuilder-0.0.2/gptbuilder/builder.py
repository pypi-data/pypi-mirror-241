import os
import json
import sys

from tqdm import tqdm
from dataclasses import dataclass
from typing import Type, Union, Optional, Dict

from .config import OpenaiConfig, AzureConfig
from .logger import logger
from .utils import generate_save_file_path, generate_response_key, handle_token_limit, save_batch, save_output
from .api import BatchAPI

@dataclass
class JsonBuilder:
    #required
    config: Union[Type[OpenaiConfig], Type[AzureConfig]]
    input_file_path: str
    system_prompt: str
    user_prompt: str
    format_dict: Dict[str, str]

    #optional
    save_file_path : Optional[str] = None
    batch_size: Optional[int] = None
    save_batch: Optional[bool] = False
    response_key: Optional[str] = 'gpt_output'
    json_encoding: Optional[str] = 'utf-8-sig'

    def __post_init__(self):
        #config
        if not isinstance(self.config, (OpenaiConfig, AzureConfig)):
            raise ValueError("config should be an OpenaiConfig or AzureConfig")
        #input file path
        if not self.input_file_path.endswith(".json"):
            raise Exception("JsonBuilder only accepts JSON files.")
        #save file path
        if self.save_file_path == None:
            self.save_file_path = generate_save_file_path()
            logger.info(f"The save path has been generated randomly:'{self.save_file_path}'")
        else:
            directory, _ = os.path.split(self.save_file_path)
            if not os.path.exists(directory):
                os.mkdir(directory)
            if os.path.exists(self.save_file_path):
                raise Exception("save_file_path already exists. Please specify some other path")
            if not self.save_file_path.endswith(".json"):
                raise Exception("save_file_path must end with .json")
        #format_dict
        if self.format_dict:
            if not all(isinstance(key, str) and isinstance(value, str) for key, value in self.format_dict.items()):
                raise ValueError("All keys, values in the format_dict must be strings.")
            else:
                try:
                    self.user_prompt.format(**self.format_dict)
                except KeyError:
                    raise Exception("The keys in format_dict do not match the format in the user_prompt.")
        if self.batch_size:
            if not isinstance(self.batch_size, int):
                raise ValueError("batch_size must be int type")
        #response_key
        if type(self.response_key)!=str:
            self.response_key = str(self.response_key)


    def _load_data(self):
        with open(self.input_file_path, 'r', encoding=self.json_encoding) as f:
            data = json.load(f)
        if not (isinstance(data, list) and all(isinstance(item, dict) for item in data)):
            raise TypeError("The JSON data is not a list of dictionaries.")
        if self.format_dict:
            for value in self.format_dict.values():
                if value not in data[0].keys():
                    raise ValueError(f"format_dict value is not in data keys, please check again.")
        if self.response_key in data[0].keys():
            self.response_key = generate_response_key(self.response_key, data[0].keys())
            logger.info(f"response_key is {self.response_key}by random")
        #check token length:
        data_config = {"data": data,
                      "config": self.config.to_handel_token(),
                      "system_prompt": self.system_prompt,
                      "user_prompt": self.user_prompt,
                      "format_dict": self.format_dict,
                      }
        load_succeeded, load_failed = handle_token_limit(data_config) 
        if len(load_failed) > 0:
            logger.info(f"{len(load_failed)}data that exceed the {self.config.model} maximum token length")
        return load_succeeded, load_failed
    
    def _make_batch(self, data):
        if self.batch_size==None:
            self.batch_size = self.config.model_tpm//self.config.model_max_token
            logger.info(f"batch_size is {self.batch_size} by default(model_tpm//model_max_token)")
        batch_data = [data[i:i+self.batch_size] 
                    if i+self.batch_size <= len(data) else data[i:]
                    for i in range(0, len(data), self.batch_size)]
        return batch_data

    def run(self):
        load_succeeded, load_failed = self._load_data()
        batch_data = self._make_batch(load_succeeded)
        success = []
        failed = []
        for idx, data in tqdm(enumerate(batch_data), desc=f"Running {len(batch_data)} Batch", total=len(batch_data)):
            try:
                api = BatchAPI(
                    client = self.config.to_client(),
                    params = self.config.to_params(),
                    system_prompt=self.system_prompt,
                    user_prompt=self.user_prompt,
                    format_dict=self.format_dict,
                    response_key=self.response_key,
                    data = data
                )
                success.extend(api.request())
            except Exception as e:
                if idx==0:
                    logger.error(e)
                    sys.exit(1)
                else:
                    logger.error(e)
                    logger.info(f"Failed-{idx}th batch")
                    failed.extend(data)
            if self.save_batch:
                save_batch(success,  self.save_file_path, self.json_encoding)
        if len(failed)>0:
            logger.info(f"{len(failed)} failed data")
        #Save output
        save_config = {
                    "input_file_path": self.input_file_path,
                    "model": self.config.model,
                    "temperature": self.config.temperature,
                    "system_prompt": self.system_prompt,
                    "user_prompt": self.user_prompt,
                    "format_dict": self.format_dict,
                    "response_key": self.response_key
                       }
        save_output(self.save_file_path, self.json_encoding, save_config, load_failed, success, failed)
        logger.info(f"Saved Output: {self.save_file_path}")