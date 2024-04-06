# -*- coding: utf-8 -*-


#import sensenova

import time
import jwt

ak =  "2eJZlgzMhSfVaR8SiZt846bMPiK" # 填写您的ak
sk = "CbduleVacPUIBZAcVNRmN50GtDzyy4M3" # 填写您的sk
notes = []

def encode_jwt_token(ak, sk):
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    payload = {
        "iss": ak,
        "exp": int(time.time()) + 1800, # 填写您期望的有效时间，此处示例代表当前时间+30分钟
        "nbf": int(time.time()) - 5 # 填写您期望的生效时间，此处示例代表当前时间-5秒
    }
    token = jwt.encode(payload, sk, headers=headers)
    return token

API_TOKEN = encode_jwt_token(ak, sk)


#sensenova.access_key_id = "2eJZlgzMhSfVaR8SiZt846bMPiK"
#sensenova.secret_access_key = "CbduleVacPUIBZAcVNRmN50GtDzyy4M3"
'''
res = sensenova.File.list()
print(res)
resp = sensenova.Model.list()
print(resp)
'''
import requests

#API_TOKEN ="nR5cCI6IkpXVCJ9.eyJpc3MiOiIyZUpabGd6TWhTZlZhUjhTaVp0ODQ2Yk1QaUsiLCJleHAiOjE3NDc2OTE3MDQsIm5iZiI6MTcxMTY5MTY5OX0.j2JtygLKXPtu3Q9bDBR0BPHJAroAT_pQqaHDKhzO_DE"
def nova_answer(info):

    url = 'https://api.sensenova.cn/v1/llm/chat-completions'  
    data = {
        "model": "nova-ptc-xl-v1",
        "Messages": [
            {
                "role": "system",
                "content": "你是专家"
            },
            {
                "role": "user", 
                "content": info
            }
        ],
        "top_p": 0.6,
        "num_of_return": 1,
        "max_new_tokens": 1024,
        "repetition_penalty": 1.2,
        "stream":False,
        "know_ids": [
            "s2e2be28169bd49e3b304dba296c85336",
            "s5d90510c385a46c2aa28812fdc6a7ead"
        ],        
        "knowledge_config": {
            "control_level": "normal", 
            "knowledge_base_result": True,
            "knowledge_base_configs": [
            {
                "know_id": "s2e2be28169bd49e3b304dba296c85336",
                "faq_threshold": 0.8
            },
            {
                "know_id": "s5d90510c385a46c2aa28812fdc6a7ead",
                "faq_threshold": 0.8
            }
            ]
        },
        "plugins":{
            "web_search": {
                "search_enable": False,
                "result_enable": False
            }#,
#            "associated_knowledge": {
#                "content": "",
#                "mode": "concatenate"
#            }
        }
    }  
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_TOKEN
    }

    response = requests.post(url, headers=headers, json=data)

#    print(response.status_code) 
    re = response.json()
    return re['data']['choices'][0]['message'] 
