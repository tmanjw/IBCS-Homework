from random import random, triangular
import matplotlib.pyplot as plt
import math

male=84
female=91
year=0
starvebaserate=0.1

xcoords=[]
ym=[]
yf=[]
yt=[]

alive=True
total=male+female
count=0
while alive==True:

    if total!=0:
        currentstarverate=starvebaserate*math.log(total,10)
    else:
        alive=False
        print('Death by Famine')

    for j in range(0,female):
        if random()<=female*0.6*0.3:
            if random()<0.5:
                female+=1
            else:
                male+=1
    female=int(female*0.95)
    male=int(male*0.95)

    for j in range(0,male):
        if random()<=currentstarverate:
            male-=1
    for j in range(0,female):
        if random()<=currentstarverate:
            female-=1

    total = male + female
    if total>1000 and count>=5:
        alive=False
    if total>1000 and count<5:
        count+=1
    year+=1
    print('Year', year, ':', total)
    xcoords+=[year]
    ym+=[male]
    yf+=[female]
    yt+=[total]

print('Final Year :', year)
print('Total Humans :',total)

plt.xlabel('Year')
plt.ylabel('Population')
plt.plot(xcoords,yt,'m',label='Total')
plt.plot(xcoords,ym,'c',label='Male')
plt.plot(xcoords,yf,'b',label='Female')
plt.legend(loc='upper left')
plt.title('Hopetopia Population')
plt.show()