import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

def ask_openai(message, system_prompt):
    response = openai.ChatCompletion.create(
        model="openai/gpt-3.5-turbo",  # Модель для OpenRouter
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY"),  # <-- Обязательное указание ключа
    )
    return response.choices[0].message.content.strip()
