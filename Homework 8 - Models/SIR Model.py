from random import random, triangular
import matplotlib.pyplot as plt
import math

susceptible=0.999
infected=0.001
recovered=0
dead=0
deathrate=0.02
beta=0.5
gamma=0.1
steps=100

graphsusceptible=[]
graphinfected=[]
graphrecovered=[]
graphdead=[]
graphsteps=[]

for i in range(0,steps):
    graphsusceptible+=[susceptible]
    graphinfected+=[infected]
    graphrecovered+=[recovered]
    graphdead+=[dead]
    graphsteps+=[i]

    newinfected=beta*infected*susceptible
    newrecovered=gamma*infected
    newdead=infected*deathrate

    susceptible-=newinfected
    infected+=(newinfected-newrecovered-newdead)
    recovered+=newrecovered
    dead+=newdead

graphsusceptible+=[susceptible]
graphinfected+=[infected]
graphrecovered+=[recovered]
graphdead+=[dead]
graphsteps+=[steps]

print(susceptible,infected,recovered)

plt.xlabel('Steps')
plt.ylabel('Fraction of Population')
plt.plot(graphsteps,graphsusceptible,'m',label='Susceptible')
plt.plot(graphsteps,graphinfected,'c',label='Infected')
plt.plot(graphsteps,graphrecovered,'b',label='Recovered')
plt.plot(graphsteps,graphdead,'r',label='Dead')
plt.legend(loc='upper left')
plt.title('Infection Spread')
plt.show()