import numpy as np

arr_1d = np.array([1,2,3])
print("1D Array:", arr_1d)

arr_2d = np.array([[1,2,3],[4,5,5]])
print("2D Array:\n", arr_2d)

zeros = np.zeros((2,3))
print("Array of Zeros:\n", zeros)

full = np.full((2,2),3)
print("Full Array:\n", full)

random = np.random.random((2,2))
print("Random Array:\n", random)

arr = np.array([[1,2,3],[4,5,6]])

print("Shape", arr.shape)
print("Data Type:", arr.dtype)
print("Size:", arr.size)
print("Number of Dimensions:", arr.ndim)

#slicing
arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print("Speccific Element:",arr_2d[2,1])
print("Row Slice:",arr_2d[1])
print("Column Slice:",arr_2d[:,2])

#Sorting
unsorted_arr = np.array([3,1,2])
print("Unsorted Array:", unsorted_arr)
sorted_arr = np.sort(unsorted_arr)
print("Sorted Array:", sorted_arr)

arr2d_unsorted = np.array([[3,2,1],
                          [6,5,4]])
sorted_arr2d = np.sort(arr2d_unsorted, axis=1)
print("Sorted 2D Array along rows:", sorted_arr2d)

#filtering
arr = np.array([1,2,3,4,5,6])
even = arr[arr % 2 == 0]
print("Even Numbers:", even)

#filter with mask
mask = arr > 3
print("Elements greater than 3:", arr[mask])

#where clause
arr = np.array([10,20,30,40,50])
result = np.where(arr > 25, "Greater than 25", "25 or less")
print("Where Clause Result:", result)

#adding elements
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concatenate((arr1, arr2))
print("Concatenated Array:", arr3)

origginal = np.array([[1,2],[3,4],[5,6]])
newrow = np.array([[7,8]])
expanded = np.vstack((origginal, newrow))
print("Original Array:", origginal)
print("Array after adding new row:", expanded)

newcol = np.array([[9],[10],[11],[12]])
expanded_col = np.hstack((expanded, newcol))
print("Array after adding new column:", expanded_col)

#deleting elements
arr = np.array([1,2,3,4,5])
arr_deleted = np.delete(arr, 2)
