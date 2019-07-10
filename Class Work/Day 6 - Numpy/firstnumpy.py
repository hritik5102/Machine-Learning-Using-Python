# #pip install numpy
# #first method
# ''' 
#import numpy as np 

# ar1 = np.array([1,2,3,4,5,5])
# print(ar1)
# '''


from numpy import array,zeros,ones,eye
# ar2 = array([1,2,3,4,5,6,7,8,9,10,11,12])
# #print(ar2)

# list = [[1,2,3,4,5,6],[4,5,6,8,3,2]]
# ar5 =  array(list)
# print(ar5[0][0])

# print(ar5.shape)

# ar1 = ar1.reshape(4,3)
# print(ar1)
# print(ar1.shape)

# ar1 = ar1.flatten()

# print(ar1)

# # print(type(ar1))

# # print(ar1 < 5)
# # print(ar1[ar1<5])
# print(ar2)
# ar3 = ar1 % ar2 # ar1+ar2
# print(ar3) 

# ar1 = array([[2.1,3.1,2.2],[4.4,5.5,6.2]])
# print(ar1)
# print(ar1.ndim)
# print(ar1.size)
# print(ar1.itemsize)
# print(ar1.dtype)
# print(ar1.nbytes)

zero1 = zeros((5,5),int)
print(zero1)

one1 = ones((5,5),int)
print(one1)

eye1 = eye(7)
print(eye1)