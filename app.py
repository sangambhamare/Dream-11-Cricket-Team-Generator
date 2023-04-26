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

    # Create a white background image
    white = np.zeros_like(image)
    white.fill(255)

    # Invert the edges and convert to 3 channels
    edges = cv2.bitwise_not(edges)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Copy the original image onto the white background, using the edges as a mask
    result = np.where(edges != 0, edges, white)
    result = cv2.bitwise_and(image, result)

    # Display the original and outline images
    col1, col2 = st.columns(2)
    col1.subheader("Original Image")
    col1.image(image, channels="BGR")

    col2.subheader("Outline Image")
    col2.image(result, channels="BGR")
