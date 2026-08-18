# import library
import numpy as np
import tensorflow as tf

# Training data(And gate)
X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([[0],[0],[0],[1]])

# Single neuron=Perceptron
model=tf.keras.Sequential([tf.keras.layers.Dense(units=1,activation="sigmoid",input_shape=(2,))])

# compile
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),loss="binary_crossentropy",metrics=["accuracy"])

#Train
model.fit(X,y,epochs=200,verbose=1)

# Predication
probability=model.predict(X)
print(probability)

# convert probability into class

prediction=(probability>= 0.5).astype(int)
print("Class:")
print(prediction)