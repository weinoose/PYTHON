import nltk
import json
import numpy
import config
import random
import numpy as np
from snowballstemmer import TurkishStemmer

# NLTK Part.

with open(config.FILE_NAME, config.METHOD, encoding=config.ENCODING) as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []
stemmer=TurkishStemmer()

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stemWord(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

output = []
training = []
out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    wrds = [stemmer.stemWord(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = numpy.array(training)
output = numpy.array(output)

# TensorFlow Part

from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Dense,Dropout

model = Sequential()
model.add(Dense(16,input_shape=(len(training[0]),),activation="relu"))
model.add(Dense(16,activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(4,activation="softmax"))
model.summary()
model.compile(Adam(lr=.001),loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(training, output,epochs=250, verbose=2,batch_size=4)

# Final NLTK Part.

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stemWord(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def chat():
    irregular = 0
    print(config.WELCOME)
    while True:
        inp = input()
        if inp.lower() == config.QUIT:
            break

        results = model.predict(np.asanyarray([bag_of_words(inp, words)]))[0]
        print(results)
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.85:
            
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            print(random.choice(responses))
        else:
            irregular += 1
            try:
                print(config.WRONG_LIST[irregular])
            except (IndexError):
                print(config.EXIT)
                break

chat()
