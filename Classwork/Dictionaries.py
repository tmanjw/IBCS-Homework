import random
import math

dict={}
for i in range(10):
    dict[i]=[]

for j in range(10000):
    var1=random.uniform(0,9)
    dict[int(var1)]+=[var1]

print(dict)