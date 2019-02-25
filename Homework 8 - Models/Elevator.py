from random import triangular
import matplotlib.pyplot as plt

#Variables that can be changed to manipulate the elevator
floors=2
height=3
speed=1
weight=10
endtime=120
#This variable changes the time of day
hour=7

#Lists used for the graphing
timeg=[]
positiong=[]
people=[]
waitingpeople=[]
liftpeople=[]
gonepeople=[]

#Variables that need to be reset before the while loop
elevatorpos=0
elevatorweight=0
totalpeople=0
leave=0
time=0
waiting=0
inlift=0
# enter=False

#While loop that runs the functions
while time<endtime+1:
    timeg+=[time]

    #Time change
    if time%60==0:
        hour+=1
        print(hour)
    if hour==24:
        hour=0

    #Determining how many people should be joining the queue to use lift
    if (hour>=6 and hour<=8) or (hour>=11 and hour<=1) or (hour>=18 and hour<=20):
        newpeople = int(triangular(1,5,2))
    else:
        newpeople = int(triangular(0,10,5))

    #The rate at which people join the queue
    if time%2 == 0:
        totalpeople += newpeople
        waiting += newpeople

    #Determing where the elevator is and which direction it should go
    if elevatorpos == 0:
        leave += inlift
        inlift = 0

        #Determining how many people can fit into the elevator, whether it's all of them or if cap has been reached
        if waiting >= weight:
            inlift += weight
            waiting -= weight
        else:
            inlift += waiting
            waiting = 0

        direction = 'Up'

    elif elevatorpos == floors*height:
        direction = 'Down'

    #Determines the actual place where the elevator is
    if direction == 'Up':
        elevatorpos += speed
    else:
        elevatorpos -= speed

    #Variables that need to be updated by end of the loop and appending variables to lists for later use in graphing
    time += 1
    positiong += [elevatorpos]
    people += [totalpeople]
    waitingpeople += [waiting]
    liftpeople += [inlift]
    gonepeople += [leave]

#Display of data in the terminal
print('Time :', timeg)
print('Position :', positiong)
print('Waiting :', waitingpeople)
print('Inlift :', liftpeople)
print('Gone :', gonepeople)
print('Total :', people)

#Plotting of data as a graph, people against time
plt.xlabel('Time')
plt.ylabel('People')
plt.plot(timeg,waitingpeople,'m',label='Waiting')
plt.plot(timeg,liftpeople,'c',label='Inside Lift')
plt.plot(timeg,gonepeople,'b',label='Left Lift')
plt.plot(timeg,people,'r',label='Total')
plt.legend(loc='upper left')
plt.title('People Using Lift')
plt.show()