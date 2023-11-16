import numpy as np

from kalapaocr.tool.vocab import Vocab
from kalapaocr.tool.img_proc import is_empty_image
from kalapaocr.dataloader import DataGen
from kalapaocr.utils import calculate_attention, load_graph_onnx


def softmax(x, axis=-1):
    """Compute softmax values for each sets of scores in x."""
    sum_exp = np.sum(np.exp(x), axis=axis)
    eta = np.ones_like(sum_exp) * (1e-7)
    return np.exp(x) / (sum_exp + eta)


class OcrEngine:
    def __init__(self, cnn_path, encoder_path, decoder_path, vocab):
        self.cnn_session = load_graph_onnx(cnn_path)
        self.encoder_session = load_graph_onnx(encoder_path)
        self.decoder_session = load_graph_onnx(decoder_path)
        self.vocab = Vocab(vocab)
        self.session = (self.cnn_session, self.encoder_session, self.decoder_session)

    def translate_onnx(
        self, img, session, max_seq_length=100, sos_token=1, eos_token=2
    ):
        """data: BxCxHxW"""
        cnn_session, encoder_session, decoder_session = session

        # create cnn input
        cnn_input = {cnn_session.get_inputs()[0].name: np.asarray(img, dtype="float16")}
        src = cnn_session.run(None, cnn_input)

        # create encoder input
        encoder_input = {
            encoder_session.get_inputs()[0].name: np.asarray(src[0], dtype="float32")
        }
        encoder_outputs, hidden = encoder_session.run(None, encoder_input)
        translated_sentence = [[sos_token] * len(img)]
        char_probs = [[1] * len(img)]

        max_length = 0
        batch_char_locations = []
        while max_length <= max_seq_length and not all(
            np.any(np.asarray(translated_sentence).T == eos_token, axis=1)
        ):
            tgt_inp = np.array(translated_sentence)
            decoder_input = {
                decoder_session.get_inputs()[0].name: tgt_inp[-1],
                decoder_session.get_inputs()[1].name: hidden,
                decoder_session.get_inputs()[2].name: encoder_outputs,
            }

            output, hidden, attention_weights = decoder_session.run(None, decoder_input)

            output = np.expand_dims(output, axis=1)
            output = softmax(output)
            indices = np.argmax(output, axis=-1)[:, -1]
            indices = indices.tolist()
            values = np.max(output, axis=-1)[:, -1]
            values = values.tolist()
            char_probs.append(values)

            translated_sentence.append(indices)
            char_locations = calculate_attention(
                image=img, attention_weights=attention_weights, index=max_length
            )
            if max_length == 0:
                batch_char_locations = char_locations
            else:
                batch_char_locations = np.concatenate(
                    (batch_char_locations, char_locations), axis=1
                )
            max_length += 1

            del output

        translated_sentence = np.asarray(translated_sentence).T
        char_probs = np.asarray(char_probs).T
        char_probs_accumulate = np.multiply(char_probs, translated_sentence > 3)
        char_probs_accumulate = np.sum(char_probs, axis=-1) / (char_probs > 0).sum(-1)
        return (
            translated_sentence,
            char_probs,
            char_probs_accumulate,
            batch_char_locations,
        )

    def predict(self, line_list, batch_size=8):
        dataset = DataGen(
            line_list, image_height=64, image_max_width=1024, batch_size=batch_size
        )
        dataloader = dataset.gen(batch_size)
        list_res = []
        for batch_dict in dataloader:
            batch = batch_dict["img"]
            list_idx = batch_dict["list_idx"]
            list_ratio = batch_dict["ratio_list"]
            s, list_probs, probs, batch_locations = self.translate_onnx(
                np.array(batch), self.session
            )
            sents = self.vocab.batch_decode(s.tolist())
            list_sent = list(
                zip(
                    sents,
                    list_idx,
                    probs.tolist(),
                    list_probs.tolist(),
                    batch_locations.tolist(),
                    list_ratio,
                )
            )
            list_res += list_sent
        list_res.sort(key=lambda x: x[1])
        return list_res

    def batch_prediction(self, line_list, batch_size=8):
        """Predict OCR results

        Args:
            line_list (numpy array): list cropped line images from original image
            batch_size (int, optional): Defaults to 8.

        Returns:
            tuple: list linelevel OCR results is extracted from list cropped line images,
        """
        if len(line_list) == 0:
            return [], []

        line_extractes = []
        text_recoged_line_list = []
        for idx, img in enumerate(line_list):
            if is_empty_image(img):
                line_extractes.append(
                    {
                        "text": "",
                        "prob": 0.99,
                        "list_probs": [0.99],
                        "locations": [],
                        "ratio": 1.0,
                        "rect": [0, 0, img.shape[1], img.shape[0]],
                    }
                )
            else:
                text_recoged_line_list.append((img, idx))

        if len(text_recoged_line_list) != 0:
            list_res = self.predict(text_recoged_line_list, batch_size=batch_size)

            for res, idx, prob, list_probs, locations, ratio in list_res:
                line_extracted = {}
                line_extracted["text"] = res
                line_extracted["prob"] = prob
                line_extracted["list_probs"] = list_probs
                new_locations = [int(location / ratio) for location in locations]
                line_extracted["locations"] = new_locations
                line_extracted["ratio"] = ratio
                line_extracted["rect"] = [
                    0,
                    0,
                    line_list[idx][0].shape[1],
                    line_list[idx][0].shape[0],
                ]
                line_extractes.append(line_extracted)

        return line_extractes
