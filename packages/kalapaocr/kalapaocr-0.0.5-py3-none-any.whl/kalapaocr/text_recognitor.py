from typing import *
import json

import numpy as np

from .recognize import OcrEngine
from .tool.postprocess import (
    postprocess_privince,
    parser_geo_json,
    postprocess_ocr_with_keywords,
    hard_postprocess,
)


class TextRecognitor:
    def __init__(
        self, cnn_path, encoder_path, decoder_path, vocab=None, street_json_path=None
    ):
        if vocab is None:
            vocab = "aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
        self.text_recogition = OcrEngine(
            cnn_path, encoder_path, decoder_path, vocab=vocab
        )
        self.data_parser = parser_geo_json(street_parser_path=street_json_path)

    def __call__(self, image: np.ndarray) -> str:
        """Input list cropped line image and rectangle coordinates perspective
        Output List Dictionary object contains ocr result with live level and word level

        :param image: line image
        :type image: np.ndarray
        :return: ocr result
        :rtype: str
        """
        res = self.text_recogition(
            img=image, image_height=64, image_max_width=1200, image_min_width=32
        )
        res = postprocess_ocr_with_keywords(res)
        res = hard_postprocess(res)
        res = postprocess_privince(res, self.data_parser)
        res = hard_postprocess(res)
        return res
