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