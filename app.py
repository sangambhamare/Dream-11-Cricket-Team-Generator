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

    # Apply bilateral filter to smooth the grayscale image
    smooth = cv2.bilateralFilter(gray, 9, 75, 75)

    # Extract edges from the smoothed image using Canny edge detection algorithm
    edges = cv2.Canny(smooth, 100, 200)

    # Create a mask by applying a threshold to the edges
    mask = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY_INV)[1]

    # Apply a bilateral filter to the original image to reduce noise and preserve edges
    cartoon = cv2.bilateralFilter(image, 9, 250, 250)

    # Apply the mask to the cartoon image to reveal only the edges
    cartoon = cv2.bitwise_and(cartoon, cartoon, mask=mask)

    # Display the original image, grayscale image, smoothed image, edges, and cartoon image
    st.subheader("Original Image")
    st.image(image, channels="BGR")

    st.subheader("Grayscale Image")
    st.image(gray, channels="GRAY")

    st.subheader("Smoothed Image")
    st.image(smooth, channels="GRAY")

    st.subheader("Edges")
    st.image(edges, channels="GRAY")

    st.subheader("Cartoon Image")
    st.image(cartoon, channels="BGR")
