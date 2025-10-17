# llm_handler.py
from llama_cpp import Llama

class LLMHandler:
    def __init__(self, model_path, max_tokens=300):
        """
        model_path: path to your GGUF model
        max_tokens: max tokens per generation
        """
        self.max_tokens = max_tokens
        self.model = Llama(
            model_path=model_path,
            n_ctx=2048,       # context length
            n_threads=4,      # adjust based on your CPU cores
            n_gpu_layers=0    # 0 for CPU-only
        )

    def generate_reply(self, prompt):
        """
        Generates a response from the LLaMA GGUF model.
        """
        response = self.model(
            prompt,
            max_tokens=self.max_tokens,
            temperature=0.8,
            top_p=0.95,
            stop=["\nUser:", "\nTalia:"]
        )
        return response['choices'][0]['text'].strip()
