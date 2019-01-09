import pygame
from pygame import gfxdraw
from random import randint
from GridworldFunctions import GridWorld

simulation = GridWorld(60,40,10)
susceptible=(108,13,196)
infected=(230,50,204)
recovered=(147,112,219)
dead=(210,210,250)
colours=[susceptible,infected,recovered,dead]
for i in range(0,300):
    simulation.set_cell(randint(0,60),randint(0,40),colours[randint(0,3)])
for cell in simulation.cells:
    print(cell[0],cell[1],simulation.cells[cell])

done=False
while not done:
    done = simulation.process_events()
    simulation.update()
