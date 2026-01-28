'''8. Write a Python program to convert a list and tuple into arrays.
List to array:
[1 2 3 4 5 6 7 8]
Tuple to array:
[[8 4 6]
[1 2 3]]'''
import numpy as np
from numpy.ma.core import reshape

lst_data = [1, 2, 3, 4, 5, 6, 7, 8]
tuple_data = [8, 4, 6, 1, 2, 3]
list_to_array = np.array(lst_data, dtype = int)
tuple_to_array = np.array(tuple_data, dtype = int).reshape(2,3)
print(list_to_array)
print(tuple_to_array)