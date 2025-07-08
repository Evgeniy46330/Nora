import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(prompt, system_prompt=""):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=1000,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
