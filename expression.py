def expression():
    import math
    V0 = 10
    a = 2.5
    z = 13/3
    V = V0*(1-(z/(math.sqrt(((a**2) + (z**2))))))
    print "When z = 4/3, V = " + str(V) + "."
    z = 13
    V = V0*(1-(z/(math.sqrt(((a**2) + (z**2))))))
    print "When z = 13, V = " + str(V) + "!"
    