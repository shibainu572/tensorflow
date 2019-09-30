from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential()

# ユニット数が64の全結合をモデルに追加する
model.add(layers.Dense(64, activation='relu'))
# 全結合層をもう一つ追加する
model.add(layers.Dense(64, activation='relu'))
# 出力ユニット数が10のソフトマックス層を追加する。
model.add(layers.Dense(10, activation='softmax'))