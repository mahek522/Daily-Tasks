'''5. Write a Python program to create a 2d array with 1 on the border and 0 inside.
Expected Output:
Original array:
[[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]]
1 on the border and 0 inside in the array
[[ 1. 1. 1. 1. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 1. 1. 1. 1.]] '''
import numpy as np

arr = np.ones((5,5), dtype = int)
print(arr)
arr[1:-1, 1:-1] = 0
print(arr)




























#print(arr)
#ar = np.array([[1, 2],[ 3, 4]])
#print(ar.transpose())
#print(ar)
#ar = np.array([[[1,2],[3,4]]])
#print(ar.shape)
#swap = ar.swapaxes(0,1)
#print(swap)
#print(ar)
#print(swap.shape)
#a = np.array([1,2])
#b = np.array([3,4])
#combine1 = np.concatenate((a,b))
#print(combine1)
#combine2 = np.vstack((a,b))
#print(combine2)
#combine3 = np.hstack((a,b))
#print(combine3)
#print(np.stack((a,b), axis=1))
#print(np.stack((a,b), axis=0))
#a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#split = np.hsplit(a,4)
#print(split)
#for i in split:
#    print(i)
a = np.array([1, 2, 3])
#print(np.repeat(a,2))
#print(np.tile(a,3))
#print(np.sum(a))
#print(np.mean(a))
#print(np.std(a))
#print(np.median(a))
#print(np.min(a))
#print(np.max(a))
#print(np.var(a))
#matrix = np.array([[1, 2, 3],
                   #[4, 5, 6],
                   #[7, 8, 9]])
#print(np.sum(matrix, axis=1))
#mask = np.logical_and(matrix>5, matrix<10)
#ar1 = np.array([[1],[2],[3]])
#ar2 = np.array([[1, 2, 3]])
#ar3 = ar1 + ar2
#print(ar2)
#print(ar1)
#print(ar3)

