from typing import *

import numpy as np

from kalapaocr.recognize import OcrEngine
from kalapaocr.tool.postprocess import (
    postprocess_privince,
    parser_geo_json,
    postprocess_ocr_with_keywords,
    hard_postprocess,
)


class TextRecognitor:
    def __init__(self, cnn_path, encoder_path, decoder_path, vocab=None):
        if vocab is None:
            vocab = "aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "
        self.text_recogition = OcrEngine(
            cnn_path, encoder_path, decoder_path, vocab=vocab
        )

    def __call__(self, image: np.ndarray) -> str:
        """Input list cropped line image and rectangle coordinates perspective
        Output List Dictionary object contains ocr result with live level and word level

        :param image: line image
        :type image: np.ndarray
        :return: ocr result
        :rtype: str
        """
        line_extractes = self.text_recogition.batch_prediction(
            line_list=[image], batch_size=4
        )
        data_parser = parser_geo_json()
        line_extract = line_extractes[0]
        res = line_extract["text"]
        res = postprocess_ocr_with_keywords(res)
        res = hard_postprocess(res)
        res = postprocess_privince(res, data_parser)
        return res
