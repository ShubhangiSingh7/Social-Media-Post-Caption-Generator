# 📸 Social Media Post & Caption Generator

An intelligent web app that generates catchy, emoji-rich social media captions based on user-selected theme, tone, and optional image uploads. It uses **EasyOCR** to detect any text in the image and **Groq’s LLaMA-4 model** to generate high-quality captions.

---

## 🚀 Features

- 📷 Upload an image (optional)
- 🔍 Extracts text from image using EasyOCR
- 🎯 Choose or type your own tone (Funny, Casual, Inspirational, etc.)
- 📱 Platform-aware captions: Instagram, LinkedIn, Twitter, etc.
- 😍 Includes emojis and relevant hashtags
- ⚡ Real-time caption generation powered by Groq's LLaMA-4

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) – UI
- [Groq](https://console.groq.com/) – Language model (LLaMA-4)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) – Text extraction from images
- [Python](https://www.python.org/) – Backend logic
- [dotenv](https://pypi.org/project/python-dotenv/) – For managing API keys

---

## 🔧 Setup Instructions

### 1. Clone the repo

git clone https://github.com/ShubhangiSingh7/Social-Media-Post-Generator.git

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add your API key

GROQ_API_KEY = your_groq_api_key_here


▶️ Run the app

streamlit run app.py
