# numpy, numpy, dee-dee...
from numpy import *

# Create a two-dimensional array filled with ints 1 to 55
twoDimArr = arange(1,56).reshape(5,11)

# Some methods and slices
shape(twoDimArr)
twoDimArr[0,3:5]
twoDimArr[0,3:9]
twoDimArr[:,2]
ndim(twoDimArr)
twoDimArr.size
twoDimArr.dtype