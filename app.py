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

    # Apply bilateral filter to reduce noise and preserve edges
    color = cv2.bilateralFilter(image, 9, 30, 250)

    # Convert the filtered image to grayscale
    gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to improve contrast
    equ = cv2.equalizeHist(gray)

    # Apply unsharp masking to enhance edges and details
    blur = cv2.GaussianBlur(equ, (5, 5), 0)
    alpha = 1.5
    beta = -0.5
    usm = cv2.addWeighted(blur, alpha, equ, beta, 0)

    # Apply adaptive thresholding to make teeth white and hair clear
    th = cv2.adaptiveThreshold(usm, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    th = cv2.cvtColor(th, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels

    # Display the original and processed images
    col1, col2 = st.columns(2)
    col1.subheader("Original Image")
    col1.image(image, channels="BGR")

    col2.subheader("Processed Image")
    col2.image(th, channels="BGR")
