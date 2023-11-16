
import gradio as gr
from gradio_test3 import Test3


with gr.Blocks() as demo:
    gr.Markdown("# Change the value (keep it JSON) and the front-end will update automatically.")
    Test3(value={"message": "Hello from Gradio!"}, label="Static")


demo.launch()
