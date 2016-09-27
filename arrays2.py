import numpy as np
ones = np.ones(100)
euler = np.exp(ones)
print(euler)

degrees = range(0, 361)
degrees = np.array(degrees)
print(degrees)

radians = np.radians(degrees)
print radians

increments = np.arange(11, 17, 0.2)
print increments

increments2 = np.arange(11, 17.2, 0.2)
print increments2