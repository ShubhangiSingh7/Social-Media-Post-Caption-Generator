📸 Social Media Post & Caption Generator
An intelligent web app that generates creative social media captions based on a user-defined theme, tone, and optional image upload. It extracts text from the image (using OCR) and combines it with user input to generate engaging captions via Groq's LLaMA-4 language model.

🚀 Features
🖼️ Upload an image (optional)

🔤 Extracts visible text using EasyOCR

🎨 Choose or enter your desired tone/mood

📱 Platform-aware captions: Instagram, Twitter, LinkedIn, etc.

✨ Captions include emojis and hashtags

⚡ Powered by Groq LLaMA-4 for fast, high-quality caption generation

🛠 Tech Stack
Streamlit – UI framework

Groq API – For streaming LLaMA-4 caption generation

EasyOCR – To detect and extract text from images

Python – Backend logic

dotenv – For API key management

📦 Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/social-caption-generator.git
cd social-caption-generator
2. Install Requirements
Make sure you have Python 3.8+ installed.

bash
Copy
Edit
pip install -r requirements.txt
🔐 Environment Setup
Create a .env file in the project root:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key
You can get your API key from:
👉 https://console.groq.com

▶️ Run the App
bash
Copy
Edit
streamlit run app.py
📁 Project Structure
bash
Copy
Edit
📦social-caption-generator
 ┣ 📄app.py                    # Main Streamlit app
 ┣ 📄caption_generator.py      # Groq API integration
 ┣ 📄requirements.txt
 ┣ 📄.env                      # Contains GROQ_API_KEY
 ┗ 📄README.md
🧠 How It Works
User inputs: platform, theme, and tone

Image OCR (optional): text is extracted from uploaded image

A prompt is generated using the above

Groq’s LLaMA-4 model generates a creative caption with emojis and hashtags

Output is streamed and shown live on the UI

📸 Example Prompt Sent to Groq
yaml
Copy
Edit
Generate a social media caption for the platform: Instagram.
Theme: AI startup.
Tone: Excited.
Image shows: Launching the future of AI from a conference stage.
Include emojis and relevant hashtags.
Format like:
Caption: ...
Hashtags: ...
Emojis: ...
✨ Example Output
yaml
Copy
Edit
📝 Caption:
Launching innovation one line of code at a time 💻🚀

#AIStartup #TechRevolution #InnovateNow  
Emojis: 💻🚀🌟🔥
💡 Future Improvements
Add Hugging Face image captioning (BLIP) for deeper visual understanding

Enable voice-to-caption mode

Add download/share button for generated captions

📜 License
This project is licensed under the MIT License.
