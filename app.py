import streamlit as st
from caption_generator import generate_streamed_caption_with_image
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="📸 Social Media Caption Generator")
st.title("📸 Social Media Post & Caption Generator")

# User Inputs
platform = st.selectbox("Select Platform", ["Instagram", "LinkedIn", "Twitter", "Facebook", "Snapchat", "Threads"])
tone = st.selectbox("Select Tone / Mood", ["Professional", "Funny", "Inspirational", "Casual", "Poetic", "Excited", "Trendy"])
custom_tone = st.text_input("Or enter your own tone (optional)")
if custom_tone:
    tone = custom_tone

theme = st.text_input("Theme or keyword", placeholder="e.g., AI startup, Beach Vibes")

uploaded_image = st.file_uploader("Upload an image (optional)", type=['png', 'jpg', 'jpeg'])
image_bytes = None

if uploaded_image:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    from io import BytesIO
    img_buffer = BytesIO()
    image.save(img_buffer, format="JPEG")
    image_bytes = img_buffer.getvalue()



# Generate Caption
if st.button("Generate Caption"):
    with st.spinner("Generating..."):
        prompt = f"""
        Generate a social media post caption for {platform} with {theme} and {tone}. Include multiple hashtags 
        and multiple emojis that match the tone and theme into a single caption.
        """

        caption_area = st.empty()
        full_caption = ""

        for chunk in generate_streamed_caption_with_image(prompt, image_bytes):
            token = chunk.choices[0].delta.content or ""
            full_caption += token
            caption_area.markdown(f"{full_caption}")
