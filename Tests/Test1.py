import pygame
import time
import random

global x, y, running

screen = pygame.display.set_mode((600, 600))

x = 200
y = 200

r1 = 131
g1 = 0
b1 = 247

r2=221
g2=169
b2=247

grid = []
for xaxis in range(0, 60):
    row = []
    for yaxis in range(0, 60):
        row += [True]
    grid+=[row]
grid[30][30]=False

def right():
    global x, y, running
    if grid[int(x/10)+1][int(y/10)]==True:
        for i in range(length*10+1):
            pygame.draw.rect(screen, (r2, g2, b2), (((x+i), y), (10, 10)))
            time.sleep(0.01)
            pygame.display.update()
        x += i
        for i in range(1,length+1):
            grid[int(x/10)+i][int(y/10)]=False

def left():
    global x, y, running
    if grid[int(x / 10) - 1][int(y / 10)] == True:
        for i in range(length * 10 + 1):
            pygame.draw.rect(screen, (r2, g2, b2), (((x - i), y), (10, 10)))
            time.sleep(0.01)
            pygame.display.update()
        x -= i
        for i in range(1,length+1):
            grid[int(x/10)-i][int(y/10)]=False

def down():
    global x, y, running
    if grid[int(x/10)][int(y/10)+1]==True:
        for i in range(length*10+1):
            pygame.draw.rect(screen, (r2, g2, b2), (((x), y+i), (10, 10)))
            time.sleep(0.01)
            pygame.display.update()
        y += i
        for i in range(1,length+1):
            grid[int(x/10)][int(y/10)+i]=False

def up():
    global x, y, running
    if grid[int(x/10)][int(y/10)-1]==True:
        for i in range(length*10+1):
            pygame.draw.rect(screen, (r2, g2, b2), (((x), y-i), (10, 10)))
            time.sleep(0.01)
            pygame.display.update()
        y -= i
        for j in range(length-1):
            grid[int(x/10)][int(y/10)-j]=False



def check():
    if x+1 and y+1 and x-1 and y-1:
        running = False



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.draw.rect(screen, (r1, g1, b1), ((x, y), (10, 10)))
    pygame.display.update()
    input()

    length=random.randint(1,5)
    print("Length :",length)

    up()

    print("x :",x,"y :",y)
    print(grid[int(x / 10) - 1][int(y / 10)])
    print()
pygame.quit()