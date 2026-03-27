from openai import OpenAI
from prompt import SYSTEM_PROMPT

OPENAI_KEY = "YOUR_API_KEY"

client = OpenAI(api_key=OPENAI_KEY)

def get_meal_plan(weight: float, height: float, gender: str, goal: str, pantry: str):
    user_message = f"""
        Now here are the inputs:
        Height: {height} cm  
        Weight: {weight} kg  
        Gender: {gender}  
        Goal: {goal}
        Pantry Items: {pantry}
    """
    messages = [
        {"role" : "system", "content" : SYSTEM_PROMPT},
        {"role" : "user", "content" : user_message}
    ]

    stream = client.chat.completions.create(model="gpt-4o-mini", messages=messages, stream=True)

    content = ""

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            content += delta
            yield content