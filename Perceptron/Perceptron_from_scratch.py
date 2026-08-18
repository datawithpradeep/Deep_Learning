# PERCEPTRON FROM SCRATCH

# Step1: Inputs (feature)
x1=2
x2=3


# Step 2: Weights:

w1=4
w2=5

# Step 3: Bias
b=-20

# Step 4: Weighted Sum
z=(x1*w1)+(x2*w2)+b

print("Weighted sum(z):",z)

# Step 5: Activation Function (Step Function)
if z>=0:
    y=1
else:
    y=0

print("prediction",y)
