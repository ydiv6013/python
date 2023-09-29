# import numpy
import numpy as np

# array of list
list_array = np.array([1,2,3,4,5,6])
print(list_array)
print(list_array[0])
print(type(list_array))
# array of tuple

tuple_array = np.array((1,2,3,4,5))
print(tuple_array)
print(type(tuple_array))

array = np.array([[[1, 2, 3], [4, 5, 6]], [[11, 12, 13], [14, 15, 16]]])
print("array",array[1,1])
print(array[1])
print(type(array))
print(array.ndim)


arr = np.array([[1,2,3],[4,5,6]],ndmin=5)
print(arr)
print("dimention of an array ",arr.ndim)

ar = np.array([1,2,3,4,5,6])

print(ar[0]+ar[5])


#negative indexing
list_array = np.array([1,2,3,4,5,6])
print(list_array)
print("3rd last value is",list_array[-3])
print("last value is",list_array[-1])
print(type(list_array))



# array slicing

array1 = np.array([1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(array1[1 : ])
print(array1[ : 5])
print(array1[1:10])

# negative slicing
print(array1[-10 : -5])
print(array1[-10 :])

# step sliciing

print(array1[ : : 2])
print(array1[5: : 2])
print(array1[:10:3])

array2 = np.array([[[1, 2, 3], [4, 5, 6]], [[11, 12, 13], [14, 15, 16]]])
print(array2[1, 1:])


# data types
print(array1.dtype)
print(arr.dtype)
print(array.dtype)


arrs = np.array(['apple', 'banana', 'cherry'])
print(arrs.dtype)

# string array

array_string = np.array([1,2,3,4,5],dtype= 'S')
print(array_string)



arrerr = np.array(['1', '2', '3'])
print(arrerr.dtype)

# astype function covert the existing array into specified datatype
newarray = arrerr.astype('S')
print(newarray.dtype)


# copy of existing array

copyarray1 = array1.copy()
print(array1)
print(copyarray1)
copyarray1[8] = 80
copyarray1[5] =50
copyarray1[10]=100
copyarray1[3]=30

print(copyarray1)

# view of an array

x= copyarray1.view()
x[15]=150
x[12]=120
print(copyarray1)
print(x)
print(x.shape)
print(arr.shape)
print(array)
print(array.shape)