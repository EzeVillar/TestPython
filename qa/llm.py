import openai
import os
from dotenv import load_dotenv
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt, model="gpt-3.5-turbo", max_tokens=400):
    start = time.time()
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.2,
        )
        duration = time.time() - start
        answer = response.choices[0].message.content.strip()
        usage = response.usage
        return {
            "answer": answer,
            "tokens": usage.total_tokens,
            "prompt_tokens": usage.prompt_tokens,
            "completion_tokens": usage.completion_tokens,
            "cost": usage.total_tokens * 0.000002,
            "duration": duration
        }
    except Exception as e:
        return {"error": str(e)}