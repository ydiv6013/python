#https://numpy.org/doc/stable/user/quickstart.html

import numpy as np

numlist =[1,2,3]
print(type(numlist))

nparray = np.array(numlist)

print(type(nparray))

# return array from range from 0 to 50
print(np.arange(0,50))
# return array from range from 0 to 50 at fixed interval=5
print(np.arange(0,50,5))

# multi dimentional array.

mularray = np.zeros((5,5))

print(mularray)
print(np.ones((5,4)))

#random array

print(np.random.randint(1,100))
print(np.random.randint(1,100,10))
ran =np.random.randint(1,100,20)

print(ran,type(ran))

#maximum
print(np.max(ran))

#minimum
print(np.min(ran))

#location of returned value
print(np.argmax(ran))
print(np.argmin(ran))

#avg 

print(np.mean(ran))

#shape of an array

print(np.shape(ran))
print(np.shape(mularray))

#reshape 

print(mularray.reshape(1,25))
print(ran.reshape(4,5))

mat= np.arange(1,100,2).reshape(10,5)
print(mat)

#retrieve valua at perticular position

print(mat[0,3])
print(mat[6,4])
print(mat[:,4])
print(mat[:,1])
print(mat[2,:])
print(mat[5,:])
print(mat[0:2,0:3])


print(mat[:,4].shape)
print(mat[:,4].reshape(2,5))

# assign a value

mat[0:3,0:2]= 0

print(mat)

#copy original matrix

newmat = mat.copy()
print(newmat)