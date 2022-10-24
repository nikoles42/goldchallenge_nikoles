import gradio as gr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re

def _count_vocal(s):
    s.lower()
    list_vocal = ['a','i','u','e','o']
    total_char = []
    for vocal in list_vocal:
        total_char.append(s.count(vocal))
    
    fig = plt.figure()
    plt.bar(list_vocal,total_char)
    plt.title("jumlah huruf vocal")
    plt.xlabel("huruf vocal")
    plt.ylabel("jumlah")
    return fig

def _remove_punct(s):
    fig = _count_vocal(s)
    return re.sub(r"[^\w\d\s]+", "",s), fig

gradio_ui = gr.Interface(
    fn=_remove_punct,
    title="simple interface",
    inputs=[gr.Textbox(label="input text")],
    outputs=[gr.Textbox(label="output text"),gr.Plot()]
)

gradio_ui.launch()