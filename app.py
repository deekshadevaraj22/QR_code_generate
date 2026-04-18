import streamlit as st
import qrcode
import io

st.title("🔳 QR Code Generator")

option = st.radio("Select Input Type:", ["Text", "Image URL"])

# -------- TEXT INPUT --------
if option == "Text":
    text = st.text_area("Enter text")

    if st.button("Generate QR"):
        if text:
            qr = qrcode.make(text)
            buf = io.BytesIO()
            qr.save(buf)
            st.image(buf.getvalue(), caption="QR Code")

# -------- IMAGE URL INPUT --------
elif option == "Image URL":
    img_url = st.text_input("Enter Image URL")

    if st.button("Generate QR"):
        if img_url:
            qr = qrcode.make(img_url)
            buf = io.BytesIO()
            qr.save(buf)
            st.image(buf.getvalue(), caption="QR Code for Image URL")

            st.success("Scan QR to open the image link!")
