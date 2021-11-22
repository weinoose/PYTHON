# Gathering modules we need.
import cv2 # To image processing.
import tensorflow as tf # Machine Learning module to create neural networks.
from tensorflow import keras # Machine Learning module to create neural networks.
from random import randint # To create random integers.
import numpy as np
import matplotlib.pyplot as plt 

def stats():
    # Gathering models with mnist.
    # Splitting the models between test and train.
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Scaling our data.
    X_train = tf.keras.utils.normalize(X_train, axis=1)
    X_test = tf.keras.utils.normalize(X_test, axis=1)

    # Creating our neural network.
    # Using two hidden layers and each of them has 16 neurons.
    # Added one flattened final input for pixel recognition.
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

    # Compiling the whole thing. 
    # Selecting > Optimizer Function, Loss Funciton and Metrics.
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Fitting the train and test data.
    model.fit(X_train, y_train, epochs=5)

    # Evaluating the model for the final result.
    loss, accuracy = model.evaluate(X_test, y_test)

    print(f"\n\nAverage loss is: {loss}") # To show loss we got.
    print(f"Accurary is: {accuracy}") # To show accuracy we got.

    askk = input("\n\nWould you like to save the model (y/n) ?: ")
    if askk == "y":
        model.save('digits.model') # Saving the model but not necessary.
    elif askk == "n":
        pass
    else:
        print("\n\nWrong choice, Model couldn't saved.")

def mnist():
    # Gathering models with mnist.
    # Splitting the models between test and train.
    (X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data() 

    # Scaling our data to range [0,1]
    X_train = X_train / 255
    X_test = X_test / 255

    # Flatting the test data
    X_train_flattened = X_train.reshape(len(X_train), 28*28)
    X_test_flattened = X_test.reshape(len(X_test), 28*28)

    # Creating our neural network.
    model = keras.Sequential([
        keras.layers.Dense(units = 128, input_shape=(784,), activation='sigmoid'),
        keras.layers.Dense(units = 128, input_shape=(784,), activation='sigmoid')
    ])

    # Compiling the whole thing. 
    # Selecting > Optimizer Function, Loss Funciton and Metrics.
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # Fitting the train and test data.
    model.fit(X_train_flattened, y_train, epochs=10)

    loss, accuracy = model.evaluate(X_test_flattened, y_test)

    print(f"\n\nAverage loss is: {loss}") # To show loss we got.
    print(f"Accurary is: {accuracy}\n\n") # To show accuracy we got.

    askk = input("Would you like to save the model (y/n) ?: ")
    if askk == "y":
        model.save('digits.model') # Saving the model but not necessary.
    elif askk == "n":
        pass
    else:
        print("\n\nWrong choice, Model couldn't saved.")

    # Picking a random handwrite digit to predict.
    randomm = randint(0, 99)

    # Realizing the real time photo of digit prediction.
    y_predicted = model.predict(X_test_flattened)
    plt.matshow(X_test[randomm])
    print(f"\n\nPrediction is : {np.argmax(y_predicted[randomm])}\n\n")

def identify(nameimage):
    # Gathering models with mnist.
    # Splitting the models between test and train.
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Scaling our data.
    X_train = tf.keras.utils.normalize(X_train, axis=1)
    X_test = tf.keras.utils.normalize(X_test, axis=1)

    # Creating our neural network.
    # Using two hidden layers and each of them has 16 neurons.
    # Added one flattened final input for pixel recognition.
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

    # Compiling the whole thing. 
    # Selecting > Optimizer Function, Loss Funciton and Metrics.
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Fitting the train and test data.
    model.fit(X_train, y_train, epochs=5)

    # Evaluating the model for the final result.
    loss, accuracy = model.evaluate(X_test, y_test)

    print(f"\n\nAverage loss is: {loss}") # To show loss we got.
    print(f"Accurary is: {accuracy}") # To show accuracy we got.

    # Load custom images to predict them.
    try:
        img = cv2.imread(nameimage)[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"\n\nThe number is probably a {np.argmax(prediction)}\n\n")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
        print()
        print()
    except:
        print(f"There is no image named {nameimage}.\n\n")

    askk = input("Would you like to save the model (y/n) ?: ")
    if askk == "y":
        model.save('digits.model') # Saving the model but not necessary.
    elif askk == "n":
        pass
    else:
        print("\n\nWrong choice, Model couldn't saved.")