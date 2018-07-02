import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop

epochs=10
batch_size=128
verbose=1

(x_train, y_train),(x_test, y_test) = mnist.load_data() #mnist資料型態

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
#Processing Character Image
