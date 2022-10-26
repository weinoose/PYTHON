from keras import models
from keras import layers
from keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

network = models.Sequential()

(train_img, train_lab), (test_img, test_lab) = mnist.load_data()

layer = layers.Dense(32, input_shape = (28 * 28, ))

network.add(layers.Dense(64, activation='relu', input_shape = (28 * 28, )))
network.add(layers.Dense(64, activation='relu', input_shape = (28 * 28, )))
network.add(layers.Dense(64, activation='relu', input_shape = (28 * 28, )))
network.add(layers.Dense(64, activation='relu', input_shape = (28 * 28, )))
network.add(layers.Dense(10, activation = 'softmax'))

print(f"\n\n{network.summary()}\n\n")

network.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

train_img = train_img.reshape((60000, 28 * 28))
train_img = train_img.astype('float32') / 255

test_img = test_img.reshape((10000, 28 * 28))
test_img = test_img.astype('float32') / 255

train_lab = to_categorical(train_lab) 
test_lab = to_categorical(test_lab)

network.fit(train_img, train_lab, epochs = 10)

loss, accuracy = network.evaluate(test_img, test_lab)

print(f"\n\nAverage loss is: {loss}")
print(f"Accurary is: {accuracy}\n\n")