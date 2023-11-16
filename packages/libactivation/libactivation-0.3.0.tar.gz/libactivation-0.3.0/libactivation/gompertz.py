# Gompertz
from numpy import exp
def gompertz(x, a=1, b=1, c=1):
    return(a*exp(-b*exp(-c*x)))
