import numpy as np
def quadratic(a, b, c):
    if b**2 - 4*a*c >= 0:
        x1 = (-1*b + np.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-1*b - np.sqrt(b**2 - 4*a*c))/(2*a)
        print "(" + str(x1) + "," + str(x2) + ")"
    else:
        y = (-1*b)/(2*a)
        z = np.sqrt(-1*(b**2 - 4*a*c))/(2*a)
        print str(y) + " + " + str(z) + "i"