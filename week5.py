import numpy as np

a1 = np.random.randint(100, size=(3))
a2 = np.random.randint(100, size=(4))
print(a1)
print(a2)
a3 =np.concatenate((a1, a2))
print(a3)


# arr1 = np.random.randint(100, size=(12))
# print(arr1)
# print("====")
# arr2 = arr1.reshape(2, 6)
# print(arr2)
# print("====")
# arr3 = arr1.reshape(3, 4)
# print(arr3)
# print("====")
# arr4 = arr1.reshape(4, 3)
# print(arr4)
# print("====")
# arr5 = arr1.reshape(6, 2)
# print(arr5)
# print("====")


# print("=====")
# arr2 = random.randint(100, size=(6, 4))
# print(arr2)
# print("=====")
# arr3 = random.randint(100, size=(2, 3, 4))
# print(arr3)

