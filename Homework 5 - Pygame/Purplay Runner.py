#7. Wandering Purplay Pixel
import pygame
import time
import random

global x, y, running, wasd, direction

screen = pygame.display.set_mode((620, 620))

x = random.randint(1,5)*100
y = random.randint(1,5)*100

r = 131
g = 0
b = 247

def empty(direction):
    global x,y,running
    if screen.get_at((x-10,y)) == (r, g, b) and screen.get_at((x+10,y)) == (r,g,b) and screen.get_at((x,y+10)) == (r,g,b) and screen.get_at((x,y-10)) == (r,g,b):
        print("Game Over")
        running=False
        input()
    elif screen.get_at((x,y-10)) != (r,g,b) and direction=='up':
        y-=10
    elif screen.get_at((x,y+10)) != (r,g,b) and direction=='down':
        y+=10
    elif screen.get_at((x-10,y)) != (r,g,b) and direction=='left':
        x-=10
    elif screen.get_at((x+10,y)) != (r,g,b) and direction=='right':
        x+=10

wasd={}
wasd['w']='up'
wasd['a']='left'
wasd['s']='down'
wasd['d']='right'

length=1

pygame.draw.rect(screen, (r, g, b), ((0, 0), (620, 10)))
pygame.draw.rect(screen, (r, g, b), ((0, 0), (10, 620)))
pygame.draw.rect(screen, (r, g, b), ((0, 610), (620, 10)))
pygame.draw.rect(screen, (r, g, b), ((610, 0), (10, 620)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    direction=wasd[random.choice('wasd')]

    for i in range(0, length):
        empty(direction)
        pygame.draw.rect(screen, (r, g, b), ((x, y), (10, 10)))

        time.sleep(0.01)
        pygame.display.update()

    print("Length :", length)
    print('Direction :', direction)
    print("x :",x,"y :",y)
    print()

    length=random.randint(1, 5)
pygame.quit()