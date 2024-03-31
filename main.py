import torch
from ctransformers import AutoModelForCausalLM
from gradio import Interface

print("Loading model...")
llm = AutoModelForCausalLM.from_pretrained("./models/phind-codellama-34b-v2.Q4_K_M.gguf", model_type="llama", gpu_layers=48, context_length=16384, max_new_tokens=16384, stream=True)
print("Model loaded.")

def make_entity(message, history):
  prompt = "typescript a {} Entity class".format(message)

  texts = []
  for text in llm(prompt, stream=True):
    print(text, end="")
    texts.append(text)

  return "".join(texts)

print("Starting server...")
demo = Interface(fn=make_entity, inputs="text", outputs="markdown")
demo.launch()
print("Server started.")
