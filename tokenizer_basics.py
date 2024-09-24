import tensorflow as tf
import keras
from keras_preprocessing.text import Tokenizer


sentences = ['What is Natural Language Processing?',
             'I am Artificial Intelligence!']

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(sentences)
word_idx = tokenizer.word_index

print(word_idx)