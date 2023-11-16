import math
import os
from collections import defaultdict

import numpy as np
from PIL import Image
from prefetch_generator import background


def resize(w, h, expected_height, image_min_width, image_max_width):
    ratio = expected_height / float(h)
    new_w = int(expected_height * float(w) / float(h))
    # round_to = 10
    # new_w = math.ceil(new_w/round_to)*round_to
    new_w = max(new_w, image_min_width)
    new_w = min(new_w, image_max_width)

    return new_w, expected_height, ratio


def process_image(image, image_height, image_min_width, image_max_width):
    img = image.convert("RGB")

    w, h = img.size
    new_w, image_height, ratio = resize(
        w, h, image_height, image_min_width, image_max_width
    )

    img = img.resize((new_w, image_height))
    img = np.asarray(img).transpose(2, 0, 1)
    img = img / 255
    return img, ratio


class BucketData(object):
    def __init__(self):
        self.max_label_len = 0
        self.data_list = []
        self.label_list = []
        self.ratio_list = []

    def append(self, datum, label, ratio):
        self.data_list.append(datum)
        self.label_list.append(label)
        self.ratio_list.append(ratio)

        return len(self.data_list)

    def flush_out(self):
        """
        Shape:
            - img: (N, C, H, W)
            - tgt_input: (T, N)
            - tgt_output: (N, T)
            - tgt_padding_mask: (N, T)
        """
        # encoder part
        img = np.array(self.data_list, dtype=np.float32)

        rs = {"img": img, "list_idx": self.label_list, "ratio_list": self.ratio_list}
        self.data_list, self.label_list, self.ratio_list = [], [], []
        return rs

    def __len__(self):
        return len(self.data_list)

    def __iadd__(self, other):
        self.data_list += other.data_list
        self.label_list += other.label_list

    def __add__(self, other):
        res = BucketData()
        res.data_list = self.data_list + other.data_list
        res.label_list = self.label_list + other.label_list
        return res


class DataGen(object):
    def __init__(
        self,
        list_img,
        image_height=32,
        image_min_width=32,
        image_max_width=512,
        batch_size=1,
        transforms=None,
    ):
        self.image_height = image_height
        self.image_min_width = image_min_width
        self.image_max_width = image_max_width
        self.batch_size = batch_size
        self.transforms = transforms
        self.lines = list_img
        self.clear()

    def clear(self):
        self.bucket_data = defaultdict(lambda: BucketData())

    @background(max_prefetch=1)
    def gen(self, batch_size, last_batch=True):
        # np.random.shuffle(self.lines)
        for img, idx in self.lines:
            img_bw = Image.fromarray(img).convert("RGB")
            img_bw, ratio = process_image(
                img_bw, self.image_height, self.image_min_width, self.image_max_width
            )
            # try:
            #     img_bw = Image.fromarray(img).convert('RGB')
            #     img_bw = process_image(img_bw, self.image_height, self.image_min_width, self.image_max_width)
            # except:
            #     print('ioread image')
            #     continue

            width = img_bw.shape[-1]

            bs = self.bucket_data[width].append(img_bw, idx, ratio)
            if bs >= batch_size:
                b = self.bucket_data[width].flush_out()
                yield b

        if last_batch:
            for bucket in self.bucket_data.values():
                if len(bucket) > 0:
                    b = bucket.flush_out()
                    yield b

        self.clear()

    def __len__(self):
        return len(self.lines) // self.batch_size
