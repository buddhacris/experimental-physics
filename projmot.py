def prjmot(t):
    g = 9.8
    v0 = 5.4
    h0 = 1.2
    v = v0 - g*t
    print ("The velocity is " + str(v) + " m/s.")
    h = h0 + v0*t - 0.5*g*(t**2)
    print ("The height is " +str(h) + " meters.")