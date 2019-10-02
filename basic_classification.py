from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and keras
import tensorflow as tf
import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# ・train_imagesとtrain_laels配列に学習のためのデータモデルをセットします。
# ・modelはtest_imagesとtest_labelsに総じてテストします。
 
# イメージは28X28のNumPy配列で、各要素は0~255の値をもってます。
# 要素のラベルは0~9までの整数の値をもっています。こちらのラベルは画像が表す衣類のクラスと一致します。
# 表は　https://www.tensorflow.org/tutorials/keras/classification　を参照
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

## Explore the data
# Lets's explore the format of the dataset before training the model.
# The following shows there are 60,000 images in the training set, with each image represented as 28X28 pixels:
print("train_images.shape : ", train_images.shape)

# 以下のprintされたように、60,000ラベルがtraingにせっとされています。
print("len(train_labels) : ", len(train_labels))

#どんなラベルも0~9の間の整数になってます。
print("train_labels : ", train_labels)

## データの前処理
# dataは networkで学習されるためには、先ず前処理が必要となります。
# 一番目のイメージを学習セットすると、ピクセルの値が0~255の範囲にあることをわかる。

# 確認するイメージのpixel array
print("len(train_images)", len(train_images))
print("len(train_images[0]) : ", len(train_images[0]))
print("len(train_images[0][0]) : ", len(train_images[0][0]))
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()