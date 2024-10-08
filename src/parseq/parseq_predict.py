from typing import List
import torch
import statistics
from PIL import Image


@torch.inference_mode()
def predict_parseq(parseq, img_transform, image, device='cuda:0'):

    # if isinstance(image, List):
    #     image = torch.stack([img_transform(img) for img in image]).to(device)
    # else:
    #     image = img_transform(image).unsqueeze(0).to(device)

    image = img_transform(image).unsqueeze(0).to(device)

    p = parseq(image).softmax(-1)
    pred, p = parseq.tokenizer.decode(p)

    return (pred, statistics.mean(p[0].tolist()))


@torch.inference_mode()
def predict_parseq_author(parseq, img_transform, image) -> tuple:
    
    predict_image = img_transform(image).unsqueeze(0)
    logits = parseq(predict_image)
    pred, prob = parseq.tokenizer.decode(logits.softmax(-1))

    return (pred, statistics.mean(prob[0].tolist()))