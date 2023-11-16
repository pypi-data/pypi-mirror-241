# logistic
from numpy import exp
def logistic(x, k=1, x0=0):
    return(1 / (1+exp(-k*(x-x0))))
