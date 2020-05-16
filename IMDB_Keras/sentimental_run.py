# load and evaluate a saved model
from numpy import loadtxt
from keras.models import load_model
from keras.datasets import imdb
from nltk import word_tokenize
from keras.preprocessing import sequence


def sentimantal_analysis(sentence):
    model = load_model('sentimantal_model.h5')
    word2index = imdb.get_word_index()
    test=[]
    for word in word_tokenize(sentence):
        test.append(word2index[word])
    max_review_length = 1000
    test=sequence.pad_sequences([test],maxlen=max_review_length)
    result = model.predict(test)
    return result[0]


if __name__ == "__main__":
    while(True):
        sentence =input("Enter your sentence: ")
        analysis_result = sentimantal_analysis(sentence)
        print(analysis_result[0])
        
