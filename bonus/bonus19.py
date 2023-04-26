import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

# Add expander to start camera:
with st.expander("Start Camera"):
    # Start the camera. Take picture shows up on website
    camera_image = st.camera_input("Camera")

# If the picture was taken:
if camera_image:
    # Create pillow image instance
    img = Image.open(camera_image)

    # Convert pillow image to gray scale
    gray_camera_img = img.convert("L")

    # Render new gray scaled image
    st.image(gray_camera_img)

if uploaded_image:
    # Create pillow image instance
    img = Image.open(uploaded_image)

    # Convert pillow image to gray scale
    gray_uploaded_img = img.convert("L")

    # Render new gray scaled image
    st.image(gray_uploaded_img)

