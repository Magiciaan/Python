import math
def d(a,b,c,d):
    e = a - b
    f = c - d
    g = e ** 2 + f ** 2
    d = math.sqrt(g)
    return d
print(d(1,2,3,4))