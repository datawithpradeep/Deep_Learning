# import numpy
import numpy as np

# input
X=np.array([2,3])

# Weights
w=np.array([4,5])

#Bias
b=-20

#Weighted Sum
z=np.dot(X,w)+b

#Step Function
prediction= 1 if z>=0 else 0
print("Weighted Sum:",z)
print("Prediction:",prediction)


