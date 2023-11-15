
import gradio as gr
from gradio_test2 import Test2


example = Test2().example_inputs()

demo = gr.Interface(
    lambda x:x,
    Test2(),  # interactive version of your component
    Test2(),  # static version of your component
    examples=[[example]],  # uncomment this line to view the "example version" of your component
)


demo.launch()
