
import gradio as gr
from gradio_textwithattachments import TextWithAttachments
from gradio_textwithattachments.textwithattachments import TextWithAttachmentsData


example = TextWithAttachments().example_inputs()


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            text = TextWithAttachments()
        with gr.Column():
            with gr.Row():
                message = gr.Textbox()
                files = gr.Files(file_count="multiple")
            with gr.Row():
                json_outout = gr.JSON()
    
    @gr.on(
    [text.text_change, text.file_upload, text.text_submit],
    inputs=[text],
    outputs=[message, files, json_outout])
    def update(data: TextWithAttachmentsData):
        return data.text, [f.name for f in data.attachments], data
             

demo.launch()
