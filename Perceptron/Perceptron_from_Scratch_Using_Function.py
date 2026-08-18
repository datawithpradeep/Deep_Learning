def perceptron(x1,w1,x2,w2):
    # Weighted sum
    z=(w1*x1)+(w2*x2)+b
    if z>=0:
        return 1
    else:
        return 0
# Input
x1=2
x2=3

# Weight
w1=4
w2=5

# Bias
b=-20

# Prediction
output=perceptron(x1,w1,x2,w2)
print("Prediction=",output)