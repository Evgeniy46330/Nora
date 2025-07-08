import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"  # ← теперь всегда используется OpenRouter!

def ask_openai(message, system_prompt):
    response = openai.ChatCompletion.create(
        model="openai/gpt-3.5-turbo",  # ← правильно!
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
