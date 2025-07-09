# 📸 Social Media Post & Caption Generator

A Streamlit web app that generates catchy, tone-aware social media captions based on:
- Platform (Instagram, LinkedIn, etc.)
- Theme or keywords
- Tone/Mood (Funny, Professional, Poetic, etc.)
- Optional image input for context (via multimodal Groq API)

---

## 🚀 Features

- 🌐 Platform-specific caption generation
- 🎭 Tone and mood customization
- 🖼️ Supports optional image input for better context
- 🔤 Includes relevant emojis and hashtags
- 🧠 Powered by Groq's `llama-4-maverick-17b-128e-instruct` model
- ⚡ Live streamed responses using the Groq API

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – for UI
- [Groq API](https://console.groq.com/) – for text + image prompt generation
- [Pillow (PIL)](https://pillow.readthedocs.io/) – for image processing
- [Base64](https://docs.python.org/3/library/base64.html) – for image encoding
- [python-dotenv](https://pypi.org/project/python-dotenv/) – to manage secrets

---

## 🔧 Setup Instructions

### 1. Clone the repo

git clone https://github.com/ShubhangiSingh7/Social-Media-Post-Caption-Generator.git

### 2. Install dependencies

pip install -r requirements.txt

### 3. Set up your environment variables

GROQ_API_KEY = your_groq_api_key_here

---

▶️ Run the app

streamlit run app.py

---

✨ Demo 

link : https://social-media-post-caption-generator-9epnrxg4u3bs27jsteqgre.streamlit.app/
