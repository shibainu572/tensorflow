from __future__ import absolute_import, division, print_function, unicode_literals

#Install TensorFlow

from keras import datasets
from keras import Sequential
from keras import layers

# Load and prepare the MNIST dataset
mnist = datasets.mnist

# CIFAR10 画像分類
# 10のクラスにラベル付けされた、50,000枚の32x32訓練用カラー画像、10,000枚のテスト用画像のデータセット
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0;

# Build the keras.Sequential model by stacking layers. Choose an optimizer and loss function fo training
# ここで使われるレイヤーの詳細を知るためには https://keras.io/ja/layers/core/ を参考しよう
model = Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])



model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train and evaluate the model :
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)