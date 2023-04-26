import streamlit as st
import numpy as np
import cv2

st.title("Cartoonify Your Image")

# Function to cartoonify the image
def cartoonify_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median blur to smoothen the image
    gray = cv2.medianBlur(gray, 5)

    # Detect edges in the image using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to the image to reduce noise while preserving edges
    color = cv2.bilateralFilter(image, 9, 250, 250)

    # Combine the color and edges to get the cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# Streamlit app code
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Read the uploaded image using OpenCV
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

    # Call the cartoonify_image function to get the cartoonified image
    cartoon = cartoonify_image(image)

    # Display the original and cartoonified image
    st.image([image, cartoon], caption=["Original Image", "Cartoonified Image"], width=500)
    
    
def cartoonify_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    cartoon = cartoonify_image(image)
    st.image([image, cartoon], caption=["Original Image", "Cartoonified Image"], width=500)    
