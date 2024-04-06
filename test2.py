import gradio as gr
import base64
import PIL.Image
# Image to Base 64 Converter
def image_to_base64(image_path):
    with open(image_path, 'rb') as img:
        encoded_string = base64.b64encode(img.read())
    return encoded_string.decode('utf-8')

# Function that takes User Inputs and displays it on ChatUI
def query_message(history,txt,img):
    if not img:
        history += [(txt,None)]
        return history
    base64 = image_to_base64(img)
    data_url = f"data:image/jpg;base64,{base64}"
    history += [(f"{txt} ![]({data_url})", None)]

# UI Code
with gr.Blocks() as app:
    with gr.Row():
        image_box = gr.Image(type="filepath")
   
        chatbot = gr.Chatbot(
            scale = 2,
            height=750
        )
    text_box = gr.Textbox(
            placeholder="Enter text and press enter, or upload an image",
            container=False,
        )


    btn = gr.Button("Submit")
    clicked = btn.click(query_message,
                        [chatbot,text_box,image_box],
                        chatbot
                        )
app.queue()
app.launch(debug=True)