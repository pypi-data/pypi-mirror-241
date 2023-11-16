import tiktoken
import json
import os
import copy
from typing import List



def generate_save_file_path()->str:
    num = 1
    cwd = os.getcwd()
    random_save_file = os.path.join(cwd, f"output_{num}.json")
    while os.path.exists(random_save_file):
        num += 1
        random_save_file = os.path.join(cwd, f"output_{num}.json")
    return random_save_file

def generate_response_key(response_key: str, dict_keys: List[str])->str:
    num = 1
    while response_key in dict_keys:
        response_key = response_key+str(num)
        num += 1
    return response_key

def count_token(prompts: List[str], start_token_length=0)->int:
    encoding = tiktoken.get_encoding("cl100k_base")
    token_length = sum([int(len(encoding.encode(prompt))) for prompt in prompts])
    token_length += start_token_length
    return token_length

def save_batch(data, file_path, json_encoding):
    directory, file_name = os.path.split(file_path)
    file_path = os.path.join(directory, "batch_"+file_name)
    with open(file_path, 'w', encoding=json_encoding) as f:
        json.dump(data, f,indent=4, ensure_ascii=False)

def save_output(file_path, json_encoding, save_config, load_failed, succes, failed):
    output = dict()
    meta_data = copy.deepcopy(save_config)
    meta_data["num_token_exceed"] = len(load_failed)
    meta_data["num_success_data"] = len(succes)
    meta_data["num_failed_data"] = len(failed)
    output["meta_data"] = meta_data
    output["success_data"] = succes
    if len(load_failed) > 0:
        output["token_exceed_data"] = load_failed
    if len(failed) > 0:
        output["failed_data"] = failed
    with open(file_path, 'w', encoding=json_encoding) as f:
        json.dump(output, f,indent=4, ensure_ascii=False)
 
def handle_token_limit(data_config):
    base_token_length = count_token(prompts=[data_config["system_prompt"], data_config["user_prompt"]])
    model_max_token = data_config["config"]["model_max_token"]
    if data_config["config"]["output_max_length"]:
        token_threshold = model_max_token - (base_token_length+data_config["output_max_length"])
    else:
        token_threshold = model_max_token - (base_token_length+300)
    failed = []
    succeeded = []
    for d in data_config["data"]:
        prompts_length = count_token([d[v] for v in data_config["format_dict"].values()])
        if prompts_length < token_threshold:
            d_copy = copy.deepcopy(d)
            succeeded.append(d_copy)
        else:
            d_copy = copy.deepcopy(d)
            d_copy["token_length"] = prompts_length
            failed.append(d_copy)

    return succeeded, failed
