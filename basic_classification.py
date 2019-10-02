from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and keras
import tensorflow as tf
import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, trainlabels), (test_images, test_labels) = fashion_mnist.load_data()