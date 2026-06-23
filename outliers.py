import numpy as np

np.arr = np.array([1, 2, 3, 4, 5,6,7,4,8,9,20,21,17,18,15,10,23,25, 100])

Q1 = np.percentile(np.arr, 25)

Q3 = np.percentile(np.arr, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

l = []

for i in np.arr:
    if i >= lower_bound and i <= upper_bound:
        l.append(i)

arr2 = np.array(l)

print("Original Array:", np.arr)
print("Filtered Array:", arr2)