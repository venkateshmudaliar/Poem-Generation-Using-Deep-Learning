
import numpy as np
import string


# initialize weights for random distributed values
# takes input and output size
def init_weight(Mi, Mo):
    return np.random.randn(Mi, Mo) / np.sqrt(Mi + Mo)


def remove_punctuation_3(s):
    return s.translate(str.maketrans('','',string.punctuation))

# function to import poem data and return sentences and word2vec
def get_poemdata():
    word2idx = {'START': 0, 'END': 1}
    current_idx = 2
    sentences = []
    #import the text file here
    for line in open('Collection_of_poems.txt'):
        line = line.strip()
        if line:
            tokens = remove_punctuation_3(line.lower()).split()
            sentence = []
            for t in tokens:
                if t not in word2idx:
                    word2idx[t] = current_idx
                    current_idx += 1
                idx = word2idx[t]
                sentence.append(idx)
            sentences.append(sentence)
    #return sentencess as indexes and thr word2index
    return sentences, word2idx

def my_tokenizer(s):
    s = remove_punctuation_3(s)
    s = s.lower() # downcase
    return s.split()

