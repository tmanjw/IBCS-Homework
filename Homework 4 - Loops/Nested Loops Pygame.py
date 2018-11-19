#Nested Loops Extension
import pygame
import time
import random

#4. My first version
#
screen=pygame.display.set_mode((500,500))

running=True
while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(0,5):
        if x%2==0:
            for y in range(0,3):
                pygame.draw.rect(screen, (131, 0, 247), ((100*x,200*y),(100,100)))
        else:
            for y in range(0,2):
                pygame.draw.rect(screen, (131, 0, 247), ((100*x,200*y+100),(100,100)))
    pygame.display.update()
pygame.quit()



#4. Piggy style
# screen = pygame.display.set_mode((500, 500))
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     for x in range(0,600,100):
#         for y in range(0,600,100):
#             if (x==200 and x==y) or (x==400 and x==y) or (x==0 and x==y):
#                 pygame.draw.rect(screen, (255, 255, 255), ((x,y), (100 , 100)))
#             elif (y==200 and y==400-x) or (y==400 and y==400-x) or (y==0 and y==400-x):
#                 pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
#             elif (x==300 and y%200==100) or (x==100 and y%200==100):
#                 pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
#             elif (x==200 and y%200==0):
#                 pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
#             elif (y==200 and x%200==0):
#                 pygame.draw.rect(screen, (255, 255, 255), ((x, y), (100, 100)))
#
#
#     pygame.display.update()
# pygame.quit()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 5.
# screen=pygame.display.set_mode((500,500))
#
# running=True
# while running==True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     for x in range(1,6):
#         red=random.randint(131,255)
#         blue=random.randint(200,255)
#         for y in range(0,x):
#             pygame.draw.rect(screen, (red, 0, blue), (((100*x-100-(50*y)),400-100*y-1), (100, 100)))
#         pygame.display.update()
#         time.sleep(0.5)