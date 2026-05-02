import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_car_description(model, brand, model_year):
    prompt = f"Gerar uma descrição de venda para um carro {brand} {model} {model_year} em até 250 caracteres."

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=120
    )

    return response.choices[0].message.content
