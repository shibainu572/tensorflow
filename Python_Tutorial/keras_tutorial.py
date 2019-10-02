# Here is the Sequential model:
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(64, activation='relu'))
# Adds a densely-connected layer with 64 units to the model:
model.add(Dense(64, activation='relu'))
# Add another:
model.add(Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(Dense(10, activation='softmax'))