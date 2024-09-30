import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pandas as pd
import pickle
from streamlit_drawable_canvas import st_canvas 
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf
from predict import predict_digit


def addition():
    st.title("SIMPLE NEURAL NETWORK")
    st.markdown('''
        <b>
        Please draw some number in the box below (Range 0-9)
        </b>
        </div>
        ''', unsafe_allow_html=True)
    
    # Load the model
    try:
        model = load_model('mnist_model.keras')
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return 

    # Load metadata (optional)
    try:
        with open('model_metadata.pkl', 'rb') as f:
            metadata = pickle.load(f)
    except Exception as e:
        st.error(f"Error loading metadata: {e}")
        return 

    # Drawing canvas
    canvas_result = st_canvas(
        stroke_width=7, 
        stroke_color="white", 
        background_color="black",
        height=150, 
        width=150, 
        drawing_mode="freedraw", 
        key="canvas"
    )

    # If drawing is made
    if canvas_result is not None and canvas_result.image_data is not None:
        # Convert the drawing to a PIL image
        img = Image.fromarray(np.uint8(canvas_result.image_data))

        # Show the drawn image
        st.image(img, caption="Your drawn digit", width=400)

        # Predict when button is clicked
        if st.button("Predict"):
            label = predict_digit(img)  # Call your prediction function
            st.subheader(f"Number Prediction: {label}")

    
