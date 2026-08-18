# import libraries
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Input data(Xor/And/Or)
X=np.array([[0,0],[0,1],[1,0],[1,1]])

# Output data(And gate)
y=np.array([0,0,0,1])

# Create Perceptron model
model=Perceptron(max_iter=10,eta0=0.01,random_state=42)

# Train model
model.fit(X,y)

# Prediction
y_pred=model.predict(X)
print("Prediction:",y_pred)

# Accuracy
print("Accuracy:",accuracy_score(y,y_pred))

# learned weights and bias
print("Weights:",model.coef_)
print("Bias:",model.intercept_)
