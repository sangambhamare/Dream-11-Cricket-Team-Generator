import streamlit as st
import numpy as np
import cv2

st.title("Cartoonify Your Image")
        
def cartoonify_image(uploaded_file):
    gray = cv2.cvtColor(uploaded_file, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)
    color = cv2.bilateralFilter(image, 9, 30, 30)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    cartoon = cartoonify_image(image)
    st.image([cartoon], caption=["Cartoonified Image"], width=400)
    return uploaded_file

