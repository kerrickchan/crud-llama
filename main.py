import torch
from flask import Flask
from ctransformers import AutoModelForCausalLM
from markdown import markdown


print("Loading model...")
llm = AutoModelForCausalLM.from_pretrained("./models/phind-codellama-34b-v2.Q4_K_M.gguf", model_type="llama", gpu_layers=48, context_length=16384)

def hello():
  for text in llm("Hello", stream=True):
    print(text, end="")

app = Flask(__name__)

@app.get("/")
def read_root():
  texts = []

  for text in llm("Python Hello World Example", stream=True):
    print(text, end="")
    texts.append(text)

  return markdown(" ".join(texts))
