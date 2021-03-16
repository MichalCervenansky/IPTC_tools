import tensorflow as tf
import tensorflow_hub as hub
from img2tensor import convert_image
import pandas as pd

# Load model into KerasLayer
print("Load model")
module = hub.KerasLayer("https://tfhub.dev/google/bit/m-r152x4/imagenet21k_classification/1")
print("Model loaded")

image = convert_image("img.jpg")  # A batch of images with shape [batch_size, height, width, 3].
logits = module(image)  # Logits with shape [batch_size, 21843].
probabilities = tf.nn.softmax(logits)

top_k = 10
probs_np = probabilities.numpy().squeeze(axis=0)
top_k_inds = probs_np.argsort()[::-1][:top_k]
classes = open("imagenet21k_wordnet_lemmas.txt", "r").readlines()
classes = [x.strip().split(',')[0] for x in classes]
data = dict()
data["Class"] = classes
data["Probability"] = probs_np
df = pd.DataFrame(data)
df = df.groupby(["Class"]).sum().sort_values(by=['Probability'], ascending=False)

print("The input picture is classified to be:")
for k in range(top_k):
    print(df.iloc[k])
