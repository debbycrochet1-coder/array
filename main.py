import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))

#accessing elements
print(arr[0])  # Accessing the first element

#slicing
arr2 = np.array(["Martin", "Soyinka", "Nifemi"])
print(arr2[1:3])

#Numpy array shape
arr3= np.array([[1,2,3],[4,5,6]])
print(arr3.shape)

#reshape
arr4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr5= arr4.reshape(4,3)
print(arr5)

#ACTIVITY
data_type=[("name","S15"), ("class", int), ("height", float)]
students_details = [("James", 5, 48.5), ("Mary", 12, 42.10), ("John", 5, 40.11)]
students= np.array(students_details, dtype=data_type)
print("Original array: ", students)
print(" Sort by height", np.sort(students, order="height"))