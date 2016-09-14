import numpy as np
def formula(x):
    if x == "a":
        a = (2 + np.exp(2.8))/(np.sqrt(13)-2)
        return a
    elif x == "b":
        b = (1-(1+(np.log(2)**-3.5)))/(1+np.sqrt(5))
        return b
    elif x == "c":
        c = np.sin((2-np.sqrt(2))/(2+np.sqrt(2)))
        return c
