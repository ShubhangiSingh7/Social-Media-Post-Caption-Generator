import streamlit as st
from caption_generator import generate_streamed_caption
from PIL import Image
import easyocr
import numpy as np

# Page setup
st.set_page_config(page_title="📸 Social Media Caption Generator")
st.title("📸 Social Media Post & Caption Generator")

# UI Inputs
platform = st.selectbox("Select Platform", ["Instagram", "LinkedIn", "Twitter", "Facebook", "Snapchat", "Threads"])
tone = st.selectbox("Select Tone / Mood", ["Professional", "Funny", "Inspirational", "Casual", "Poetic", "Excited", "Trendy"])
custom_tone = st.text_input("Or enter your own tone (optional)")
if custom_tone:
    tone = custom_tone

theme = st.text_input("Theme or keyword", placeholder="e.g., AI startup, Beach Vibes")
uploaded_image = st.file_uploader("Upload an image (optional)", type=['png', 'jpg', 'jpeg'])
image_desc = ""

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    image = Image.open(uploaded_image)
    image_np = np.array(image)

    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(image_np)
    image_desc = ' '.join([text for _, text, _ in results])

if st.button("Generate Caption"):
    with st.spinner("Generating..."):
        # Build the prompt
        prompt = f"""Generate a social media caption for the platform: {platform}.
        Theme: {theme}.
        Tone: {tone}.
        Image shows: {image_desc}.
        Include emojis and relevant hashtags.
        Format like:
        Caption: ...
        Hashtags: ...
        Emojis: ..."""

        # Call the Groq API and stream response
        caption_area = st.empty()
        full_caption = ""

        for chunk in generate_streamed_caption(prompt):
            token = chunk.choices[0].delta.content or ""
            full_caption += token
            caption_area.markdown(f"**📝 Caption:**\n\n{full_caption}")
