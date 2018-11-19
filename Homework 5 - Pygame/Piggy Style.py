import pygame
import time
import random

snake_xy = [300, 300]
white = 255
failure = False
blue = 255
length = 0
screen = pygame.display.set_mode((620, 620))
screen.fill((0, 0, 0))

white = (0, 0, 0)


def where():
    global random_pixel, random_direction
    random_pixel = random.randint(1, 5)*10
    random_direction = random.randint(1, 4)
    length = 0
    failure = False

    while length != random_pixel and failure == False:
        if screen.get_at((snake_xy[0] + 10, snake_xy[1])) == (0, 0, blue) and screen.get_at(
                (snake_xy[0] - 10, snake_xy[1])) == (0, 0, blue) and screen.get_at((snake_xy[0], snake_xy[1] + 10)) == (
        0, 0, blue) and screen.get_at((snake_xy[0], snake_xy[1] - 10)) == (0, 0, blue):
            print("RIP")
            failure == True
            break
        elif screen.get_at((snake_xy[0], snake_xy[1] - 10)) != (0, 0, blue) and random_direction == 1:  # up
            snake_xy[1] -= 10
        elif screen.get_at((snake_xy[0], snake_xy[1] + 10)) != (0, 0, blue) and random_direction == 2:  # down
            snake_xy[1] += 10
        elif screen.get_at((snake_xy[0] - 10, snake_xy[1])) != (0, 0, blue) and random_direction == 3:  # left
            snake_xy[0] -= 10
        elif screen.get_at((snake_xy[0] + 10, snake_xy[1])) != (0, 0, blue) and random_direction == 4:  # Right
            snake_xy[0] += 10
        else:
            print("Broken")
            failure == True
            break
        length += 10
        pygame.draw.rect(screen, (0, 0, 255), (snake_xy, (10, 10)))
        print(snake_xy)
        time.sleep(0.01)
        pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, (0, 0, blue), ((0, 0), (10, 620)))
    pygame.draw.rect(screen, (0, 0, blue), ((0, 0), (620, 10)))
    pygame.draw.rect(screen, (0, 0, blue), ((610, 0), (10, 620)))
    pygame.draw.rect(screen, (0, 0, blue), ((0, 610), (620, 10)))
    pygame.display.update()

    for i in range(1, random.randint(1, 10)):
        where()

pygame.quit()