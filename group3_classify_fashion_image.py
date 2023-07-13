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
