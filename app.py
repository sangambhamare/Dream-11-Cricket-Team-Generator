import streamlit as st
import numpy as np
import cv2

st.title("Clean your Image")
        
st.set_option('deprecation.showfileUploaderEncoding', False)

# Upload an image file
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the uploaded image
    image = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection algorithm to extract the outlines
    edges = cv2.Canny(gray, 100, 200)

    # Convert the edges to 3 channels
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Display the original and outline images
    col1, col2 = st.columns(2)
    col1.subheader("Original Image")
    col1.image(image, channels="BGR")

    col2.subheader("Outline Image")
    col2.image(edges, channels="BGR")
