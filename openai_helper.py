response = openai.ChatCompletion.create(
    model="openai/gpt-3.5-turbo",  # ← правильно!
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ],
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY"),
)
