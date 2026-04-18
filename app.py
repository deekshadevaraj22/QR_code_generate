import streamlit as st
import qrcode
from PIL import Image
import io
import base64

st.title("🔳 QR Code Generator")

option = st.radio("Select Input Type:", ["Text", "Image"])

# -------- TEXT INPUT --------
if option == "Text":
    text = st.text_area("Enter text to generate QR code")

    if st.button("Generate QR"):
        if text:
            qr = qrcode.make(text)
            buf = io.BytesIO()
            qr.save(buf)
            st.image(buf.getvalue(), caption="Generated QR Code")

# -------- IMAGE INPUT --------
elif option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        # Convert image to base64 (so QR can store it)
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        if st.button("Generate QR"):
            qr = qrcode.make(img_str)
            buf = io.BytesIO()
            qr.save(buf)
            st.image(buf.getvalue(), caption="QR Code for Image")
