import streamlit as st
from caption_generator import generate_streamed_caption
from PIL import Image
import easyocr
import numpy as np

st.set_page_config(page_title="📸 Social Media Caption Generator")

st.title("📝 Caption Generator with Groq API + Image Upload")

platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter"])
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
