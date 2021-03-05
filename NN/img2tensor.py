import cv2
import math
import numpy as np


def convert_image(img_path):
    # attributes for ImageNet-1K
    # Load a testing image:
    image = cv2.imread(img_path, flags=cv2.IMREAD_COLOR)

    # Resize image with keeping aspect ratio:
    resize_value = int(math.ceil(float(224)))
    h, w = image.shape[:2]
    if not ((w == resize_value and w <= h) or (h == resize_value and h <= w)):
        resize_size = (resize_value, int(resize_value * h / w)) if w < h else (int(resize_value * w / h), resize_value)
        image = cv2.resize(image, dsize=resize_size, interpolation=cv2.INTER_LINEAR)

    # Center crop of the image:
    h, w = image.shape[:2]
    th, tw = 224, 224
    ih = int(round(0.5 * (h - th)))
    jw = int(round(0.5 * (w - tw)))
    image = image[ih:(ih + th), jw:(jw + tw), :]

    # Convert image to a float tensor and normalize it:
    x = image.astype(np.float32)
    x = x / 255.0
    return x


print(convert_image("img.jpg"))
