import sensenova
import json

sensenova.access_key_id = "2eJZlgzMhSfVaR8SiZt846bMPiK"
sensenova.secret_access_key = "CbduleVacPUIBZAcVNRmN50GtDzyy4M3"

#resp = sensenova.Model.list()
#获取http headers
#print(resp['data'])

#res = sensenova.Model.retrieve(id=model_id)
#print(res)

import sys


def return_mes(info):

    model_id ='nova-ptc-xl-v1' 
    stream = True
    resp = sensenova.ChatCompletion.create(
        messages=[{"role": "user", "content": info}],
        model=model_id,
        stream=stream,
        max_new_tokens=1024,
        n=1,
        repetition_penalty=1.05,
        temperature=0.8,
        top_p=0.7,
        know_ids=["s2e2be28169bd49e3b304dba296c85336","s5d90510c385a46c2aa28812fdc6a7ead"],
        user="cusomter service",
        knowledge_config={
            "control_level": "high",
            "knowledge_base_result": True,
            "knowledge_base_configs":[{"know_ids":"s2e2be28169bd49e3b304dba296c85336","faq_threshold":0.9},{"know_ids":"s5d90510c385a46c2aa28812fdc6a7ead","faq_threshold":0.8}]
        },
        plugins={
            "associated_knowledge": {
                "content": "需要注入给模型的知识",
                "mode": "concatenate"
            },
            "web_search": {
                "search_enable": True,
                "result_enable": True
            },
        }
    )
#    print(resp["id"])
    resp = [resp]
    
    return resp['data']['choices'][0]['message']
    
'''
    result=[]

    if not stream:
        resp = [resp]
    
    for part in resp:
        choices = part['data']["choices"]
        for c_idx, c in enumerate(choices):
            if len(choices) > 1:
                sys.stdout.write("===== Chat Completion {} =====\n".format(c_idx))
            if stream:
                delta = c.get("delta")
                if delta:
                    #sys.stdout.write(delta)
                    result.append(delta)
            else:
            #    sys.stdout.write(c["message"])
            #    if len(choices) > 1:
            #        sys.stdout.write("\n")
                result.append(c["message"])
            
    return result
'''
