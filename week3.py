# ===Exercise 3_2====
print("Exercise 3_2")
import os
if not os.path.exists("myFiles"):
    os.mkdir("myFiles")
f = open("myFiles/data1.txt", 'w')
l = [*range(0, 101)]
l = ', '.join([str(el) for el in l])
print(l)
f.write(l)
f.close()