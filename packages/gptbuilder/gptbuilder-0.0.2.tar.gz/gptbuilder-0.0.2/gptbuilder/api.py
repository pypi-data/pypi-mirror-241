import asyncio
import copy
import re
import math

import openai
from openai.types.chat.chat_completion import ChatCompletion
from openai import AsyncOpenAI, AsyncAzureOpenAI
from typing import List, Type, Union
from dataclasses import dataclass

@dataclass
class BatchAPI:
    client: Union[Type[AsyncOpenAI], Type[AsyncAzureOpenAI]]
    params: dict
    system_prompt: str
    user_prompt:str
    format_dict: dict
    response_key: str
    data: List[dict]

    def _format_user_prompt(self):
        formatted_data = []
        for d in self.data:
            format_dict_ = {}
            for key in self.format_dict.keys():
                format_dict_[key] = d[self.format_dict[key]]
            formatted_data.append(self.user_prompt.format(**format_dict_))
        return formatted_data
    
    @staticmethod
    def _parse_wait_time(error_message: str, default: int)->int:
        pattern = r"Please try again in (\d+(\.\d+)?)(ms|s)"
        match = re.search(pattern, error_message)
        if match:
            time_value, _, time_unit = match.groups() 
            wait_time = float(time_value)
            if time_unit == 'ms':
                wait_time = wait_time / 1000
            wait_time = int(math.ceil(wait_time))
        else:
            wait_time = default
        return  wait_time

    async def _async_generate(self, user_prompt):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        params = self.params
        params["messages"] = messages
        try:
            response = await self.client.chat.completions.create(**params)
        except openai.RateLimitError as error:
            wait_time = self._parse_wait_time(error.message, 3)
            await asyncio.sleep(wait_time)
            while True:
                try:
                    response = await self.client.chat.completions.create(**params)
                    break
                except openai.RateLimitError as error:
                    wait_time = self._parse_wait_time(error.message, 3)
                    await asyncio.sleep(wait_time)
        return response.choices[0].message.content
    
    async def _generate_concurrently(self):
        formatted_user_prompt = self._format_user_prompt() 
        tasks = [asyncio.create_task(self._async_generate(user_prompt)) for user_prompt in formatted_user_prompt]
        responses = await asyncio.gather(*tasks)
        outputs = copy.deepcopy(self.data)
        for i, output in enumerate(outputs):
            output[self.response_key] = responses[i]
        return outputs

    def request(self):
        result = asyncio.run(self._generate_concurrently())
        return result


