#import nova_response_func as nova
#res = nova.nova_answer("我的灯什么时候安装呢？")
#print(res)

import nova_response_his_func as nova

session_id = nova.nova_session()
res = nova.nova_answer_with_his("我的灯什么时候安装呢？",session_id)
print(res)