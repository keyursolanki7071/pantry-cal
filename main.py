import gradio as gd
from services.ai_service import get_meal_plan

height_input = gd.Textbox(label="Height (CM)", placeholder="Enter your height in cm")
weight_input = gd.Textbox(label="Weight (KG)", placeholder="Enter your weight in kg")
gender_input = gd.Radio(choices=["Male", "Female"], label="Gender")
goal_input = gd.Radio(choices=["Fat Loss", "Muscle Gain", "Maintain"], label="Goal")
pantry_items = gd.TextArea(label="Pantry Items", placeholder="Enter pantry items comma seperated")

output_box = gd.Markdown(label="You Meal Plan For Day", value="Your meal plan will appear here...", height=600, elem_id="output_box", padding=5)

title = "Pantry Cal"
description = "Create your daily meal plan based on your body stats and pantry items"
examples = [
    [80, 175, "Male", "Fat Loss", "Eggs, Milk, Oats, Raisins, Spices, Oil, Cheese, Watermelon, Paneer, Onion, Potatoes, Capsicum"],
    [55, 150, "Female", "Muscle Gain", "Paneer, Onion, Soya Chunks, Chana, Potatoes, Spices, Oranges, Chicken, Rice, Cabbage, Carrot"]
]
inputs = [weight_input, height_input, gender_input, goal_input, pantry_items]

interface = gd.Interface(fn=get_meal_plan, inputs=inputs, outputs=[output_box], flagging_mode="never", examples=examples, title=title, description=description)

interface.launch(auth=("admin", "admin"))

