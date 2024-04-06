import gradio as gr
import nova_response_func as nova
import  pdb
def yes_man(message, history,arg3,arg4,arg5):
    pdb.set_trace()
    text = message["text"]
    files = message["files"]
    context = ""
    for img_path in files:
        if text == "":
            text += ocr(img_path)
        else:
            context += ocr(img_path)
    return nova.nova_answer(text)

def ocr(image_path):
    import pytesseract
    from PIL import Image
    # Open the image
    image = Image.open(image_path)

    # Extract text from the image
    text = pytesseract.image_to_string(image)
    return text

docs = gr.Interface(lambda name: "文档" + name, "text", "text")
libs = gr.Interface(lambda name: "知识库" + name, "text", "text")

chat= gr.ChatInterface(
    yes_man,
    chatbot=gr.Chatbot(height=300,label='智能对话'),
    multimodal=True,
    # textbox=gr.Textbox(interactive=True,placeholder="请输入你的问题,图片，或者与语音", container=False, scale=7,label='智能对话'),
    # textbox = gr.MultimodalTextbox(interactive=True, file_types=["image"], placeholder="请输入你的问题,图片，或者与语音",
    #  container=False, scale=7,show_label=False),
    additional_inputs = [
        gr.CheckboxGroup(["s2e2be28169bd49e3b304dba296c85336",
            "s5d90510c385a46c2aa28812fdc6a7ead"
        ], info="选择适合的知识",label="知识库选择"),
        gr.Dropdown(choices=["中度","高度"], type="index",label="知识库控制"),
        gr.Slider(0, 1, step=0.1,label="最大新Token数")
    ],
    
    additional_inputs_accordion = gr.Accordion(label="模型参数控制", open=False),
    title="欧普智慧客服",
    description="我是欧普客服，请问我欧普相关的问题吧",
    theme="soft",
    # examples=["台灯有重影", "不同色温功率一样吗", "双头应急灯放电应急时间多久"],
    # cache_examples=False,
    retry_btn=None,
    undo_btn="删除上一条",
    clear_btn="清空",
    submit_btn=None
)
docs = gr.ChatInterface(
    yes_man,
    chatbot=gr.Chatbot(height=300,label='文档上传'),
#    multimodal=True,
    textbox=gr.Textbox(interactive=True,placeholder="请输入你的文档，格式可以是json,PDF,Excel,Word ", container=False, scale=7,label='文档'),

#    additional_inputs = gr.Textbox(),
#    additional_inputs_accordion = gr.Accordion(label="Additional Inputs", open=False),
    title="文档上传",
    description="上传文档",
    theme="soft",
    # examples=["台灯有重影", "不同色温功率一样吗", "双头应急灯放电应急时间多久"],
    # cache_examples=False,
    retry_btn=None,
    undo_btn="新增",
    clear_btn="删除",
    submit_btn="提交"
)
libs= gr.ChatInterface(
    yes_man,
     chatbot=gr.Chatbot(height=300,label='知识库维护'),
#    multimodal=True,
   textbox=gr.Textbox(interactive=True,placeholder="创建知识库", container=False, scale=7,label='创建'),
#    additional_inputs = gr.Textbox(),
#    additional_inputs_accordion = gr.Accordion(label="Additional Inputs", open=False),
    title="欧普智慧客服",
    description="我是欧普客服，请问我欧普相关的问题吧",
    theme="soft",
    # examples=["台灯有重影", "不同色温功率一样吗", "双头应急灯放电应急时间多久"],
    # cache_examples=False,
    retry_btn=None,
    undo_btn="删除知识库",
    clear_btn="新建知识库",
    submit_btn="提交"
)
demo = gr.TabbedInterface([chat, docs, libs], ["智能客服", "文档维护","知识库维护"])
demo.launch(share=True)