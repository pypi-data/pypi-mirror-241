class Vocab:
    def __init__(self, chars):
        self.pad = 0
        self.go = 1
        self.eos = 2
        self.mask_token = 3

        self.chars = chars

        self.c2i = {c: i + 4 for i, c in enumerate(chars)}

        self.i2c = {i + 4: c for i, c in enumerate(chars)}

        self.i2c[0] = "<pad>"
        self.i2c[1] = "<sos>"
        self.i2c[2] = "<eos>"
        self.i2c[3] = "*"

    def encode(self, chars):
        labels = [self.go]
        for char in chars:
            if char in self.c2i:
                labels.append(self.c2i[char])
            else:
                print("{} out of vocab".format(char))
                labels.append(self.pad)
        labels += [self.eos]
        # return [self.go] + [self.c2i[c] for c in chars] + [self.eos]
        return labels

    def decode(self, ids):
        first = 1 if self.go in ids else 0
        last = ids.index(self.eos) if self.eos in ids else None
        sent = ""
        for i in ids[first:last]:
            if i != self.pad:
                sent += self.i2c[i]
            else:
                sent += " "
        # sent = ''.join([self.i2c[i] for i in ids[first:last]])
        return sent

    def __len__(self):
        return len(self.c2i) + 4

    def batch_decode(self, arr):
        texts = [self.decode(ids) for ids in arr]
        return texts

    def __str__(self):
        return self.chars
