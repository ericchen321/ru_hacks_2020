
'''
   project sentiment analysis by using the IMDB data
   Zitian Tong
   2017.12.23

   Using the keras neural network to predict and train the model
'''


import numpy as np
import keras
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.preprocessing.text import Tokenizer
import matplotlib.pyplot as plt

np.random.seed(42)

# load the data
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=1000)

#print(x_train.shape)
#print(x_test.shape)
#print(x_train[0])
#print(y_train[0])

tokenizer = Tokenizer(num_words=1000)
x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')
#ßprint(x_train[0])
#print(x_train[0].shape)

num_classes = 2
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
#print(y_train.shape)
#print(y_test.shape)
#print(y_train[0])


# build the model
model = Sequential()

# 1st and 2nd layer
model.add(Dense(1200, activation='relu', input_shape= x_train[0].shape))
model.add(Dropout(0.5))

# 3rd layer
model.add(Dense(400, activation='relu'))
model.add(Dropout(0.5))

# 4th layer
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.4))
# output layer
model.add(Dense(num_classes, activation='softmax'))

model.summary()
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# train the model and check the result
hist = model.fit(x_train, y_train, batch_size=1000, epochs=10, validation_data=(x_test, y_test), verbose=2)

score = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: ", score[1])

model.save('sentimantal_model.h5')
