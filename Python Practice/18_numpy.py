import numpy as np
np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print(x1)
#array([5, 0, 3, 3, 7, 9])

#Multi-Dimensional
print(x2)
"""
something like
array([[3, 5, 2, 4],
       [7, 6, 8, 8],
       [1, 6, 7, 7]])
"""

print(x2[0, 0])
#3 and more examples

x2[0, 0] = 12
print(x2)
"""
array([[12,  5,  2,  4],
       [ 7,  6,  8,  8],
       [ 1,  6,  7,  7]])

Keep in mind that, unlike Python lists, NumPy arrays have a fixed type. 
This means, for example, that if you attempt to insert a floating-point value to an integer array, 
the value will be silently truncated. Don't be caught unaware by this behavior!
"""
x1[0] = 3.14159  # this will be truncated!
print(x1)
#array([3, 0, 3, 3, 7, 9])

print("x3 ndim: ", x3.ndim)
#x3 ndim:  3

print("x3 shape:", x3.shape)
#x3 shape: (3, 4, 5)

print("x3 size: ", x3.size)
#x3 size:  60

print("dtype:", x3.dtype)
#dtype: int64

print("itemsize:", x3.itemsize, "bytes")
#itemsize: 8 bytes
print("nbytes:", x3.nbytes, "bytes")
#nbytes: 480 bytes

#Array Slicing: Accessing Subarrays
#x[start:stop:step]
"""
If any of these are unspecified, they default to the values start=0, stop=size of dimension, step=1. 
We'll take a look at accessing sub-arrays in one dimension and in multiple dimensions.
"""

#One-dimensional subarrays
x = np.arange(10)
print(x)
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
"""
np.arange(3.0)
array([ 0.,  1.,  2.])
np.arange(3,7)
array([3, 4, 5, 6])
np.arange(3,7,2)
array([3, 5])
"""


print(x[:5])  # first five elements
#array([0, 1, 2, 3, 4])

print(x[5:])  # elements after index 5
#array([5, 6, 7, 8, 9])

print(x[4:7])  # middle sub-array
#array([4, 5, 6])

print(x[::2])  # every other element
#array([0, 2, 4, 6, 8])

print(x[1::2])  # every other element, starting at index 1
#array([1, 3, 5, 7, 9])

"""
A potentially confusing case is when the step value is negative. 
In this case, the defaults for start and stop are swapped. 
This becomes a convenient way to reverse an array:
"""

print(x[::-1])  # all elements, reversed
#array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(x[5::-2])  # reversed every other from index 5
#array([5, 3, 1])