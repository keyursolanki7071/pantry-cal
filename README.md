# 🥗 Pantry Cal – AI Meal Planner

Pantry Cal is a simple AI-powered web app that generates a daily meal plan based on your body stats and available pantry items.

---

## 🚀 Features

* Generate personalized meal plans
* Uses your:

  * Weight
  * Height
  * Gender
  * Fitness goal
  * Pantry items
* Simple and easy-to-use UI built with Gradio

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/pantry-cal.git
cd pantry-cal
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Add your OpenAI API Key

Open the file:

```
services/ai_service.py
```

Find this line:

```
OPENAI_KEY = "YOUR_API_KEY"
```

Replace it with your actual OpenAI API key:

```
OPENAI_KEY = "sk-xxxxxxxxxxxxxxxx"
```

👉 You can get your API key from: https://platform.openai.com/api-keys

---

### 4. Run the app

```
python main.py
```

---

## 🔐 Login Credentials

By default:

```
Username: admin
Password: admin
```

You can change this in `main.py`:

```
app.launch(auth=("admin", "admin"))
```

---

## 🛠 Tech Stack

* Python
* Gradio
* OpenAI API

---