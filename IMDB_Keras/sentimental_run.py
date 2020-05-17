# load and evaluate a saved model
import logging
from numpy import loadtxt
from keras.models import load_model
from keras.datasets import imdb
from nltk import word_tokenize
from keras.preprocessing import sequence

from queue import Queue

MAX_NUM_WORDS_PROCESSED = 5

    
# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s))  


def sentimantal_analysis(sentence):
    model = load_model("/Users/danieltong/Library/Mobile Documents/com~apple~CloudDocs/Study/Hackathon/ru_hacks_2020/IMDB_Keras/sentimantal_model.h5")
    word2index = imdb.get_word_index()
    test=[]
    for word in word_tokenize(sentence):
        test.append(word2index[word])
    max_review_length = 1000
    test=sequence.pad_sequences([test],maxlen=max_review_length)
    result = model.predict(test)
    return result[0]

def real_time_analysis(q):
    while(True):
        count = 0
        wordsList = []
        try:
            data = q.get()
            while count < MAX_NUM_WORDS_PROCESSED:
                while q.empty() is True:    # polls until we can get a word
                    pass
                word = q.get()
                print(word)
                wordsList.append(word)
                count = count + 1
            sentence = listToString(wordsList)
            print("the sentence is: " + sentence)
            print(sentimantal_analysis(sentence))
        except Exception as ex:
            logging.error("Error: {}".format(ex))

if __name__ == "__main__":
    while(True):
        sentence =input("Enter your sentence: ")
        analysis_result = sentimantal_analysis(sentence)
        print(analysis_result[0])
        
