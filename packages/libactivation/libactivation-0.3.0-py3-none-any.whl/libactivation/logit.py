# logit
from numpy import log
def logit(x):
    return(log( x / (1-x) ))
