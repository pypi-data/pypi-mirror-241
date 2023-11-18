import numpy as np

from kalapaocr.tool.vocab import Vocab
from kalapaocr.tool.img_proc import is_empty_image
from kalapaocr.utils import calculate_attention, load_graph_onnx, process_image


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

    def __call__(self, img, image_height=64, image_max_width=1024, image_min_width=64):
        if is_empty_image(img):
            return ""
        img, _ = process_image(
            img,
            image_height=image_height,
            image_max_width=image_max_width,
            image_min_width=image_min_width,
        )
        s, list_probs, probs, batch_locations = self.translate_onnx(img, self.session)
        sents = self.vocab.batch_decode(s.tolist())
        return sents[0]
        pass
