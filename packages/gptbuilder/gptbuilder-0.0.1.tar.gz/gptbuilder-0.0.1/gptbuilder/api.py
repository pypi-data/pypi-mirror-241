import asyncio
import copy

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

    async def _async_generate(self, user_prompt):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        params = self.params
        params["messages"] = messages
        response = await self.client.chat.completions.create(**params)
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



