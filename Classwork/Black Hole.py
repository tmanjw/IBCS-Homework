import random

def move(where):
    repeat=True
    while repeat==True:
        sign=''
        variable=0
        if random.randint(1,2)%2==0:
            sign='-'
        if random.randint(1,2)%2==0:
            variable=1

        new=where[variable]+int(sign+'1')
        if new<0 or new==size:
            repeat=True
        else:
            where[variable]=new
            repeat=False

    return where


size=4
x=0
y=0
here=[x,y]
goal=[size-1,size-1]
grid=[]
holes=[]

while len(holes)<3:
    holes+=[[random.randint(0,size-1),random.randint(0,size-1)]]
    holes=set(holes)
    for i in range(len(holes)):
        if holes[i]==(0,0) or holes[i]==(size-1,size-1):
            holes.pop(i)


for i in range(size):
    grid += [[]]
    for j in range(size):
        if [i, j] == here:
            grid[i] += ['Here']
        elif [i,j] == goal:
            grid[i] += ['Goal']
        elif [i,j] in holes:
            grid[i] += ['Hole']
        else:
            grid[i] += [[i, j]]

for i in range(size):
    print(grid[i])

input('[Press Enter] :')

run=True
balance=0
while run==True:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    move(here)
    if here == goal:
        balance += 25
        run = False
        print('You have reached the goal!')
        print('Total Balance :', balance)
    elif here in holes:
        run=False
    grid=[]
    if run==True:
        for i in range(size):
            grid += [[]]
            for j in range(size):
                if [i,j]==here:
                    grid[i]+=['Here']
                    balance+=1
                elif[i,j]==goal:
                    grid[i]+=['Goal']
                elif [i, j] in holes:
                    grid[i] += ['Hole']
                else:
                    grid[i] += [[i, j]]

    if run==True:
        for i in range(size):
            print(grid[i])

    input('[Press Enter] :')