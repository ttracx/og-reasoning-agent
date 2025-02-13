import openai

class LLM:
    def __init__(self):
        openai.api_key = "YOUR_OPENAI_API_KEY"

    def chat(self, prompt):
        response = openai.ChatCompletion.create(
            model="deepseek-r1",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
