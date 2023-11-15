from openai import AsyncOpenAI, AsyncAzureOpenAI

from dataclasses import dataclass
from typing import Optional

@dataclass
class OpenaiConfig:
    api_key: str
    model: str
    temperature: float
    model_max_token: int
    model_tpm: int
    output_max_length: Optional[int] = None

    def to_client(self):
        client = AsyncOpenAI(api_key=self.api_key)
        return client
    
    def to_handel_token(self):
        args = {
            "model_max_token": self.model_max_token,
            "output_max_length": self.output_max_length
        }
        return args

    def to_params(self):
        args = {
            "model": self.model,
            "temperature": self.temperature
            }
        if self.output_max_length != None:
            args["max_tokens"] = self.output_max_length
        return args
    
@dataclass
class AzureConfig:
    api_key: str
    api_version: str 
    azure_endpoint: str
    model: str
    temperature: float
    model_max_token: int
    model_tpm: int
    output_max_length: Optional[int] = None

    def to_client(self):
        client = AsyncAzureOpenAI(api_key=self.api_key,
                                  api_version=self.api_version,
                                  azure_endpoint=self.azure_endpoint)
        return client
    
    def to_handel_token(self):
        args = {
            "model_max_token": self.model_max_token,
            "output_max_length": self.output_max_length
        }
        return args

    def to_params(self):
        args = {
            "model": self.model,
            "temperature": self.temperature
        }
        if self.output_max_length != None:
            args["max_tokens"] = self.output_max_length
        return args