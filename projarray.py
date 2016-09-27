import numpy as np

g = 9.8
h0 = 10
i = 0

y = np.arange(10, 0, -0.5)
print y

t = np.array(np.sqrt(2*(h0-y)/g))

print t