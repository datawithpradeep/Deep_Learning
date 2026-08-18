# import numpy
import numpy as np

#Input Data
X=np.array([[0,0],[0,1],[1,0],[1,1]])

# Target output(OR Gate)
y=np.array([0,1,1,1])

#Initialize Weights
weights=np.zeros(2)

#Bias

bias=0

#Learning Rate
lr=0.1

# Epochs
epochs=10

for epoch in range(epochs):
    for i in range(len(X)):
        # Weighted sum
        z=np.dot(X[i],weights)+bias

        #Step Function
        prediction=1 if z>=0 else 0

        #Error
        error=y[i]-prediction

        #weight update
        weights=weights+lr*error*X[i]

        #Bias Update
        bias=bias+lr*error

print("Weighted sum:",weights)
print("Bias:",bias)
