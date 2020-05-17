import logging
from numpy import loadtxt
from keras.models import load_model
from keras.datasets import imdb
from nltk import word_tokenize
from keras.preprocessing import sequence


train, test = imdb.load_data()
tf.keras.datasets.imdb.get_word_index(path="imdb_word_index.json")
print(train[0])