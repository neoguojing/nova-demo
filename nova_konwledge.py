import sensenova

sensenova.access_key_id = "2eJZlgzMhSfVaR8SiZt846bMPiK"
sensenova.secret_access_key = "CbduleVacPUIBZAcVNRmN50GtDzyy4M3"

model_id ='nova-ptc-xl-v1' 

description="罗氏制药" #知识库描述
file_id="" #通过【文件管理】模块创建的文件id，只能是schemd="KNOWLEDGE_BASE_1"的文件
files=[file_id] #可以为空

## 创建知识库
resp = sensenova.KnowledgeBase.create(description=description,files=files)

knowledge_base_id=resp["knowledge_base"]["id"] #知识库id
## 更新知识库
resp = sensenova.KnowledgeBase.update(description=description,files=files,sid=knowledge_base_id)
## 查询知识库列表
resp = sensenova.KnowledgeBase.list()
## 查询知识库详情
resp = sensenova.KnowledgeBase.retrieve(id=knowledge_base_id)
## 删除知识库
resp = sensenova.KnowledgeBase.delete(sid=knowledge_base_id)