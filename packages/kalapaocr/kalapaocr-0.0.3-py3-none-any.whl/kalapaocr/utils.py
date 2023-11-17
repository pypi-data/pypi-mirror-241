import os

import cv2
import pandas as pd
import numpy as np
from PIL import Image
import onnxruntime as rt


def load_graph_onnx(model_path):
    sess_opt = rt.SessionOptions()
    sess_opt.graph_optimization_level = rt.GraphOptimizationLevel.ORT_ENABLE_BASIC
    session = rt.InferenceSession(
        model_path, sess_options=sess_opt, providers=["CUDAExecutionProvider"]
    )
    return session


def bmm(x, y):
    # Reshape the input tensors to have shape (batch_size, num_rows, num_cols)
    x = np.reshape(x, (x.shape[0], x.shape[1], -1))
    y = np.reshape(y, (y.shape[0], -1, y.shape[2]))

    # Compute the batch matrix-matrix product using numpy.matmul
    out = np.matmul(x, y)

    # Reshape the output tensor back to its original shape
    out = np.reshape(out, (out.shape[0], out.shape[1], -1))

    return out


def calculate_attention(image, attention_weights, index, log_dir=None, vis=False):
    batch_size = attention_weights.shape[0]
    height, width = image.shape[-2:]
    T = attention_weights.shape[1] // 2
    ct = [x for x in range(T)]
    for i in range(T):
        if i == 0:
            ct[i] = 2.5
            continue
        if i == T - 1:
            ct[i] = 2 + (i - 1 - 2) * 4 + 6 + ((width - (2 + (i - 1 - 2) * 4 + 6)) / 2)
        else:
            ct[i] = 2 + (i - 1) * 4 + 3
    ct = np.expand_dims(ct, axis=0)
    ct = np.vstack((ct, ct))
    ct = ct.transpose((1, 0))
    ct = ct.flatten()
    batch_ct = np.zeros_like(attention_weights)
    for i in range(batch_size):
        batch_ct[i] = ct
    attention_weights = np.expand_dims(attention_weights, axis=1)
    batch_ct = np.expand_dims(batch_ct, axis=-1)
    centers = bmm(attention_weights, batch_ct).squeeze(1)
    if vis and batch_size == 1:
        image = image.squeeze(0) * 255
        image = image.transpose((1, 2, 0))
        center = centers[0]
        cv2.line(
            image,
            (int(center), 0),
            (int(center), height),
            (0, 255, 0),
            thickness=3,
            lineType=8,
        )
        image_path = os.path.join(log_dir, "{}.jpg".format(index))
        cv2.imwrite(image_path, image)
    return centers


def create_submission(paths, results, output_path):
    res = {"id": [], "answer": []}
    for path, s in zip(paths, results):
        relative_path = path.split("/")[-2] + "/" + path.split("/")[-1]
        res["id"].append(relative_path)
        res["answer"].append(s)
    df = pd.DataFrame(res)
    df.to_csv(output_path, index=False)


def resize(w, h, expected_height, image_min_width, image_max_width):
    ratio = expected_height / float(h)
    new_w = int(expected_height * float(w) / float(h))
    # round_to = 10
    # new_w = math.ceil(new_w/round_to)*round_to
    new_w = max(new_w, image_min_width)
    new_w = min(new_w, image_max_width)

    return new_w, expected_height, ratio


def process_image(image, image_height, image_min_width, image_max_width):
    image = Image.fromarray(image).convert("RGB")
    img = image.convert("RGB")

    w, h = img.size
    new_w, image_height, ratio = resize(
        w, h, image_height, image_min_width, image_max_width
    )

    img = img.resize((new_w, image_height))
    img = np.asarray(img).transpose(2, 0, 1)
    img = img / 255
    img = img[np.newaxis, ...]
    return img, ratio
