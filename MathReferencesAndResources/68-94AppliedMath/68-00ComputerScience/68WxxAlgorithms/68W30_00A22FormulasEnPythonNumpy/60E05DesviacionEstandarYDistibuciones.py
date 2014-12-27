# From J. Guttag, MITx 6.002X 
import numpy

def mean(X):
    return sum(X) / float(len(X))

def variance(X):
    """
    Returns variance of list X
    """
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))

def stdDev(X):
    """
    Returns standard deviation of list X
    """
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def CV(X):
    """
    Returns coefficient of variation of list X
    """
    mean = sum(X)/float(len(X))
    try:         
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan') 

def rSquare(measured, estimated):
    """
    Returns R square, coefficient of determination.
    measured: one dimensional array of measured values
    estimate: one dimensional array of predicted values
    """
    SEE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - SEE/MV

def clusterVariance(X):
    """
    Returns cluster variance of list X
    """
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot
