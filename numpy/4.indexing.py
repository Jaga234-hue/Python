import numpy as np

arr = np.array([1, 2, 3, 4, 5]);
print(arr[0]);
print(arr[1]);
print(arr[2]);
print(arr[3]);
print(arr[4]);
print(arr[-1]);

#2D Array
print("\n \n 2D Array");
arr = np.array([[1, 2, 3],[4, 5, 6]]);
print(arr[0, 1]);#first row and second column
print(arr[1, 2]);#second row and third column
print(arr[1, -1]);#second row and last column