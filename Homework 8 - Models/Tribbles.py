from random import random, triangular
import matplotlib.pyplot as plt
import math

population=1
step=12
time=0
birthrate=0.1
deathrate=0.05
predatorrate=0.05
starveratebase=0.32

x_coords=[]
y_coords=[]

for i in range(0,6):
    if population!=0:
        currentstarverate = starveratebase * math.log(population, 10)
    else:
        currentstarverate = 0
    for j in range(0,population):
        if random()<=birthrate and population!=1:
            population+=int(triangular(1,15,10))
        else:
            population += int(triangular(1, 15, 10))

    for j in range(0, population):
        if random()<=deathrate:
            population-=1
        elif random()<=predatorrate:
            population-=1
        elif random()<=currentstarverate:
            population-=1

    x_coords.append(i*step)
    y_coords.append(population)


print(x_coords)
print(y_coords)
plt.figure()
plt.xlabel('Hours')
plt.ylabel('Population')
plt.plot(x_coords,y_coords)
plt.title('Tribble Population Growth')
plt.show()
