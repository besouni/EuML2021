#==Exercise 4_5==
text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
print(text)
text1 = text[:21]
print(text1)
s = 0
for i in text:
    if 'ს'==i:
        s = s+1
print(s)

# == String ==
# a = "Hello Students" \
#     "Hello Teachers"
# b = """
#     trings in python are surrounded by either single quotation marks,
#     or double quotation marks.
#  """
# c = "Hello Student"
# for i in c:
#     print(i)
#
# print(c[0])
# print(len(c))

# print(c.strip())
# n = "Beso"
# l = "Tabatadze"
# s = "My Name is {0}, Lastname is {1}".format(n, l)
#
# print(s)

# if "Stu" in c:
#     print("Yes")
# else:
#     print("NO")


# == Numpy ==

import numpy as np
# l = [2, 3, 4, 9]
# n0 = np.array(23)
# n1 = np.array([2, 3, 4, 9, -9, 7, 3, 7, 0, 2, -2, -4])
# print(n1)
# print(n1.dtype)

# print(n1[1:4])
# print(n1[1:])
# print(n1[:4])
# print(n1[-4:-1])
# print(n1[1:7:2])
# print(n1)
# n1[1:7:2] = 0
# print(n1)
# n1[0::2]=-1
# print(n1)

# n2 = np.array([
#                 [2, 3],
#                 [4, 9],
#                 [-9, 7]
#               ])
#
# n3 = np.array([
#                 [
#                     [2, 3, 4],
#                     [0, 8, 3]
#                 ],
#                 [
#                     [9, -9, 7],
#                     [-3, 5, 8]
#                 ]
#               ])
# print(n1[3])
# print(n2[1, 0])
# print(n2[1, -2])
# print(n3[1, 0, 0])

# print(n0)
# print(n1)
# print(n2)
# print(n3)

# print(l)
# print(n)
# print(type(n))
# print(np.__version__)
