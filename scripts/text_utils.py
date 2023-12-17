data = "../data/dialogue.txt"

with open(data, "r", encoding="utf-8") as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)

stoi = {
    ch:i for i, ch in enumerate(chars)
    }

itos = {
    i:ch for i, ch in enumerate(chars)
    }

encode = lambda s: [stoi[c] for c in s]
decode = lambda l: "".join([itos[i] for i in l])