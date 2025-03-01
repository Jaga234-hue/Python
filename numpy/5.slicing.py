import numpy as np
#syntax of slicing
# array[start:end:step]
arr = np.array([10, 20, 30, 40, 50]);
print(arr[1:4]);
print(arr[0:4:2]);
print(arr[:3]);
print(arr[2:]);
print(arr[::2])

#2D Array
arr = np.array([[1, 2, 3],[4, 5, 6]]);
# array[row_start:row_end, col_start:col_end]

print(arr[1:, :2]);  # From row index 1 onward, first two columns
print(arr[:1, 1:]);  # First two rows, from second column onward
