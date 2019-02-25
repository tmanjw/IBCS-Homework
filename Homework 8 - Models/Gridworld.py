import pygame
from pygame import gfxdraw
from random import randint
from random import random
from GridworldFunctions import GridWorld
from time import sleep

simulation = GridWorld(60,40,10)
susceptible=(108,13,196)
infected=(230,50,204)
recovered=(147,112,219)
dead=(210,210,250)
colours=[susceptible,infected,recovered,dead]

for i in range(0,300):
    simulation.set_cell(randint(0,60),randint(0,40),colours[randint(0,3)])

infecteddict={}

done=False
while not done:
    done = simulation.process_events()

    for cell in simulation.cells:
        if simulation.get_cell(cell[0],cell[1])==susceptible:

            chance = 0
            oneaway=0
            for j in simulation.get_surroundings(cell[0], cell[1], 1):
                for k in j:
                    if k == infected or k == dead:
                        oneaway+=1

            twoaway=0
            for j in simulation.get_surroundings(cell[0], cell[1], 2):
                for k in j:
                    if k == infected or k == dead:
                        twoaway+=1
            twoaway-=oneaway

            threeaway=0
            for j in simulation.get_surroundings(cell[0], cell[1], 3):
                for k in j:
                    if k == infected or k == dead:
                        threeaway+=1

            threeaway-=twoaway+oneaway
            chance=(oneaway*0.25)+(twoaway*0.05)+(threeaway*0.02)
            if chance>0.97:
                chance=0.97

            if random()<=chance:
                simulation.remove_cell(cell[0],cell[1])
                simulation.set_cell(cell[0],cell[1],infected)


        elif simulation.get_cell(cell[0],cell[1])==infected:

            if cell not in infecteddict:
                infecteddict[cell]=3
            else:
                if infecteddict.get(cell)==0:
                    if randint(0,1)==0:
                        simulation.remove_cell(cell[0],cell[1])
                        simulation.set_cell(cell[0],cell[1],dead)
                    else:
                        simulation.remove_cell(cell[0], cell[1])
                        simulation.set_cell(cell[0],cell[1],recovered)
                else:
                    infecteddict[cell]=infecteddict.get(cell)-1


    sleep(1)
    simulation.update()
