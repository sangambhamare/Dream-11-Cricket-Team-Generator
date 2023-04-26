import streamlit as st
import numpy as np
import cv2
        
# Set page icon and title
st.set_page_config(page_title='Cartoonify Image', page_icon=':lower_left_paintbrush:')        
st.title("Cartoonify Your Image")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Smoothen the grayscale image
    gray = cv2.medianBlur(gray, 5)

    # Retrieve edges of the image
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Prepare mask of the image
    color = cv2.bilateralFilter(image, 9, 250, 250)
    mask = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Add a black border to the image
    border_size = 10
    border_color = [0, 0, 0]
    image = cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=border_color)

    # Apply the cartoon effect
    output = cv2.bitwise_and(color, mask)

    # Display the original and processed images
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Original Image")
        st.image(image, channels="BGR")

    with col2:
        st.write("Cartoon Image")
        st.image(output, channels="BGR")

    with col3:
        st.write("Colored Cartoon Image")
        output_gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(output_gray, 10, 255, cv2.THRESH_BINARY)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        color_output = cv2.bitwise_and(image, mask)
        st.image(color_output, channels="BGR")
        
    st.code("© Developed by Mr. Sangam Bhamare & SQUAD. All rights reserved.")
