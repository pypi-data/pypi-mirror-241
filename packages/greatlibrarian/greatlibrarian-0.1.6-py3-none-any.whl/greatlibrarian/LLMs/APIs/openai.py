from Core import LLMs
import zhipuai

from http import HTTPStatus
import dashscope

import qianfan

class ChatGPT(LLMs):
    def __init__(self):
        self.apikey = ""
        self.name = "gpt-3.5-turbo"
    
    def __call__(self, prompt: str) -> str:
        pass

class chatglm_pro(LLMs):
    def __init__(self):
        # self.apikey = "450fe9e4faec64c0a48234a5d92115ef.aWoqpjlhWO2Kpbvw" #czy
        self.apikey = "3a447d07983428cffdef5df6d3698f8b.49I1Uyvs9pVpcgth" #dmj
        self.name = "chatglm_pro"
    
    def __call__(self, prompt: str) -> str:
        zhipuai.api_key = self.apikey
        response = zhipuai.model_api.invoke(
        model="chatglm_pro",
        prompt=[{"role": "user", "content": prompt}],
        top_p=0.7,
        temperature=0.9,
        )
        if response['code']==200:
            return(response['data']['choices'][0]['content'])
        else:
            return('API Problem')

class qwen_turbo(LLMs):
    def __init__(self):
        self.apikey = "sk-9ca2ad73e7d34bd4903eedd6fc70d0d8"
        self.name = "qwen_turbo"
    
    def __call__(self, prompt: str) -> str:
        dashscope.api_key = self.apikey
        response = dashscope.Generation.call(
        model=dashscope.Generation.Models.qwen_turbo,
        prompt=prompt
        )

        if response:
            if response['output']:
                if response['output']['text']:
                    return(response['output']['text'])
        return('API Problem')

class wenxin(LLMs):
    def __init__(self):
        self.ak="B00yKgZuin8IolPHYsHggVyU"
        self.sk="B19OtdVn0jwwaByK9RgovfukUQWv2rT6"
        self.name = "ernie-bot"
    
    def __call__(self, prompt: str) -> str:
        # 替换下列示例中参数，应用API Key替换your_ak，Secret Key替换your_sk
        chat_comp = qianfan.ChatCompletion(ak=self.ak, sk = self.sk)

        # 指定特定模型
        resp = chat_comp.do(model="ERNIE-Bot", messages=[{
            "role": "user",
            "content": prompt
        }])

        if resp:
            if resp['body']:
                if resp['body']['result']:
                    return(resp['body']['result'])
        return('API Problem')
        
chatgpt = ChatGPT()