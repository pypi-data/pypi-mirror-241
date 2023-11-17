
import gradio as gr
from gradio_gptchatbot import GPTChatbot


example = GPTChatbot().example_inputs()

with gr.Blocks() as demo:
    with gr.Row():
        GPTChatbot(label="Blank"),  # blank component
        GPTChatbot(value=example, label="Populated"),  # populated component


demo.launch()
