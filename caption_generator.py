from groq import Groq
import base64
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY") )

def generate_streamed_caption_with_image(prompt, image_bytes=None):
    messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]

    if image_bytes:
        base64_image = base64.b64encode(image_bytes).decode("utf-8")
        messages[0]["content"].append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })

    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=messages,
        temperature=0.7,
        stream=True
    )
    return response
