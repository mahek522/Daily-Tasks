'''Write a Python program to create a null vector of size 10 and update sixth value to 11.
[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.] '''
import numpy as np
arr = np.zeros(10)
print(arr)
arr[6] = 11
print(arr)