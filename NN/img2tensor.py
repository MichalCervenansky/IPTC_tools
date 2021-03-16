import cv2
import numpy as np
import tensorflow as tf

CROP_TO = 224


def preprocess_image(image):
    image = np.array(image)
    # reshape into shape [batch_size, height, width, num_channels]
    img_reshaped = tf.reshape(image, [1, image.shape[0], image.shape[1], image.shape[2]])
    # Use `convert_image_dtype` to convert to floats in the [0,1] range.
    image = tf.image.convert_image_dtype(img_reshaped, tf.float32)
    return image


def convert_image(img_path):
    # Load a testing image:
    image = cv2.imread(img_path, flags=cv2.IMREAD_COLOR)

    image = preprocess_image(image)
    image = tf.image.resize(image, [CROP_TO, CROP_TO])

    # Convert image to a float tensor and normalize it:
    x = image
    return x
