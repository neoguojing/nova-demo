import sensenova
import io
import json

sensenova.access_key_id = ""
sensenova.secret_access_key = ""

model_id ='nova-ptc-xl-v1' 

payload = {
    "text_lst": [
        "aa.pdf"
    ]
}
#file = io.StringIO(json.dumps(payload, ensure_ascii=False)) #构造一个file对象即可
#file = open('./aa.pdf','r',encoding='utf-8')
scheme="KNOWLEDGE_BASE_2" #枚举值，请参考文件管理API文档
resp = sensenova.File.create(file="./aa.pdf",scheme=scheme,description="罗氏药品")
#file.close()

file_id = resp["id"]
# 查询文件
#resp = sensenova.File.retrieve(id=file_id)
# 下载文件
#resp = sensenova.File.download(id=file_id) #resp为文件的原始内容，只有文件status="VALID"的才可以下文件内容
# 删除文件
#resp = sensenova.File.delete(id=file_id)
#文件列表
resp = sensenova.File.list()
print(resp)