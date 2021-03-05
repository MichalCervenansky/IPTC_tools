# -*- coding: utf-8 -*-

from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import decode_predictions
from numpy import expand_dims
from keras.applications.vgg16 import VGG16


def predictions_VGG16(imagePath):
    # load the model
    model = VGG16()

    img_name = imagePath
    # load the image with the required shape
    img = load_img(img_name, target_size=(224, 224))
    # convert the image to an array
    img = img_to_array(img)
    # expand dimensions so that it represents a single 'sample'
    img = expand_dims(img, axis=0)
    # prepare the image (e.g. scale pixel values for the vgg)
    img = preprocess_input(img)
    # get feature map for first hidden layer
    yhat = model.predict(img)

    # convert the probabilities to class labels and retrieve 50 of the most likely results, e.g. highest probability
    labels = decode_predictions(yhat, top=50)[0]
    # print the classification

    filter_columns = lambda label: (label[1], label[2])
    return list(map(filter_columns, labels))


predictions = predictions_VGG16("img.jpg")
for prediction in predictions:
    print('%s (%.2f%%)' % (prediction[0], prediction[1] * 100))

predictions_VGG16("img.jpg")
