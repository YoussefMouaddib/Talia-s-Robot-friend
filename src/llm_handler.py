# llm_handler.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLMHandler:
    def __init__(self, model_path, max_tokens=300, use_gpu=True):
        self.device = "cuda" if torch.cuda.is_available() and use_gpu else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto" if self.device=="cuda" else None,
            torch_dtype=torch.float16 if self.device=="cuda" else torch.float32
        )
        self.max_tokens = max_tokens

    def generate_reply(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=self.max_tokens,
            do_sample=True,
            temperature=0.8
        )
        reply = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return reply
