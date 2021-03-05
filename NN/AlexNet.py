import json
import torch
import torchvision.transforms as transforms
from PIL import Image
from alexnet_pytorch import AlexNet


def predictions_AlexNet(imagePath):
    # Open image
    input_image = Image.open(imagePath)

    # Preprocess image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

    # Load class names
    labels_map = json.load(open("AlexNet_labels_map.txt"))
    labels_map = [labels_map[str(i)] for i in range(1000)]

    # Classify with AlexNet
    model = AlexNet.from_pretrained("alexnet")
    model.eval()

    with torch.no_grad():
        logits = model(input_batch)
    preds = torch.topk(logits, k=5).indices.squeeze(0).tolist()

    res_list = []
    for idx in preds:
        label = labels_map[idx]
        prob = torch.softmax(logits, dim=1)[0, idx].item()
        res_list.append((label, prob))
    return res_list

print(predictions_AlexNet("img.jpg"))