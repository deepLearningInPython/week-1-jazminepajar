import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(number):
    if number > 0:
        return 1
    return -1

#Testing
print(step(1))

# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLu(array, cutoff = 0):
    new_array = []
    for part in array:
        if part > cutoff:
            new_array.append(part)
        else: 
            new_array.append(cutoff)
    return new_array

#Some testing
array = [0,5,3,8,-1,5]
print(ReLu(array, 2))


# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(array2, array1):
    product = np.dot(array2, array1)
    return ReLu(product)

#Some testing
x = np.array([[1, 2], [1, 2], [1, 2]])
y = np.array([1, 2])
print(neural_net_layer(x,y))

# ------------------------------------------