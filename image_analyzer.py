import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load a pre-trained image classification model (e.g., MobileNetV2)
model = tf.keras.applications.MobileNetV2(weights='imagenet')
decode_predictions = tf.keras.applications.mobilenet_v2.decode_predictions
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input

def analyze_image(image):
    # Preprocess the image for the model
    image = image.resize((224, 224))
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)
    
    # Predict the components in the image
    predictions = model.predict(image_array)
    decoded_predictions = decode_predictions(predictions, top=5)[0]  # Get top 5 predictions
    
    # Extract and return the names of the components
    component_names = [pred[1] for pred in decoded_predictions]
    return component_names

st.title("Image Component Analyzer")

# Upload image widget
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Button to analyze image
    if st.button("Analyze Image"):
        with st.spinner("Analyzing..."):
            component_names = analyze_image(image)
            st.write("Components detected in the image:")
            for name in component_names:
                st.write(f"- {name}")

