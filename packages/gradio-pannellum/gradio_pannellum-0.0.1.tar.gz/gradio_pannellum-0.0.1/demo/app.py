
import gradio as gr
from gradio_pannellum import Pannellum


example = Pannellum().example_inputs()

demo = gr.Interface(
    lambda x:x,
    Pannellum(),  # interactive version of your component
    Pannellum(),  # static version of your component
    examples=[[example]],  # uncomment this line to view the "example version" of your component
)


demo.launch()
