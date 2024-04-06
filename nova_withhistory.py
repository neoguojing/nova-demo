import sensenova
import sys

sensenova.access_key_id = "2eJZlgzMhSfVaR8SiZt846bMPiK"
sensenova.secret_access_key = "CbduleVacPUIBZAcVNRmN50GtDzyy4M3"

model_id ='nova-ptc-xl-v1' 


# 创建会话
resp = sensenova.ChatSession.create(
    system_prompt = [
        {
            "role": "system",
            "content": "You are a translation expert."
        }
    ]
)
session_id = resp["session_id"]
# 有状态对话生成
stream = True # 流式输出或非流式输出
model_id = model_id # 填写真实的模型ID
resp = sensenova.ChatConversation.create(
    action="next",
    content="地球的直径是多少米?",
    model=model_id,
    session_id=session_id,
    stream=stream,
    know_ids=[],
    knowledge_config={
        "control_level": "normal",
        "knowledge_base_result": True,
        "knowledge_base_configs":[]
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

if not stream:
    resp = [resp]
for part in resp:
    if stream:
        delta = part["data"]["delta"]
        if delta:
            sys.stdout.write(delta)
    else:
        sys.stdout.write(part["data"]["message"])
    sys.stdout.flush()