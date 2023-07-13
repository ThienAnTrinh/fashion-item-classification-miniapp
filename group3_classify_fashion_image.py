import streamlit as st
import tensorflow as tf
import numpy as np


def load_and_convert(input_path):
    """
    This function loads an image from the input path,
    converts it to grayscale, and resizes it to (28, 28).
    """
    input_image = tf.keras.utils.load_img(
        input_path,
        color_mode='grayscale',
        target_size=(28, 28),
        interpolation='nearest',
        keep_aspect_ratio=False
    )
    return input_image


def predict(category_list, model, uploaded):
    """
    This function classifies the image and shows the result in Streamlit.
    """
    if uploaded:
        input_image = load_and_convert(uploaded)
        st.image(input_image, caption="Preprocessed Image (28x28 grayscale)")
        input_array = tf.keras.utils.img_to_array(input_image)
        pred = model.predict(np.expand_dims(input_array, axis=0), verbose=0)
        pred = np.argmax(pred, axis=-1).squeeze()
        cat = category_list[pred]
        st.subheader(f"It looks like a :blue[{cat}]")
    else:
        st.error("No image has been uploaded")