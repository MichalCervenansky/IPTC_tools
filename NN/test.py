from tf2cv.model_provider import get_model as tf2cv_get_model
import tensorflow as tf
from gluoncv.data import ImageNet
import numpy as np
from NN.img2tensor import convert_image

net = tf2cv_get_model("AlexNet", pretrained=True, data_format="channels_last")
x = convert_image("img_23.jpg")
x = ((x - np.array((0.485, 0.456, 0.406))) / np.array((0.229, 0.224, 0.225))).reshape(1, 224, 224, 3)
y = net(x)
probs = tf.nn.softmax(y)

top_k = 5
probs_np = probs.numpy().squeeze(axis=0)
top_k_inds = probs_np.argsort()[::-1][:top_k]
classes = ImageNet().classes
print("The input picture is classified to be:")
for k in range(top_k):
    print("{idx}: [{class_name}], with probability {prob:.3f}.".format(
        idx=(k + 1),
        class_name=classes[top_k_inds[k]],
        prob=probs_np[top_k_inds[k]]))