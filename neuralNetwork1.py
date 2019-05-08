import tensorflow as tf
import numpy as np
from tensorflow import keras

# Create the model with 1 neuron and 1 input shape
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Compile the 2 functions: optimizer and loss. (Optimizer makes the guesses,
# Loss measures the guessed answers.)
model.compile(optimizer='sgd', loss='mean_squared_error')

# We provide the data with the numpy library.
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# fit function makes the NN learn while the epochs pass.
model.fit(xs, ys, epochs=500)

# Print the result
print(model.predict([10.0]))
