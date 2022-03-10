import pygame, sys, random
from pygame import *
from time import *
from cell import Cell

pygame.init()

screen = pygame.display.set_mode((600, 600))
display = pygame.Surface((128, 128))
clock = pygame.time.Clock()

pop = 20
cells = []
steps = 100
steps_u = 0
for i in range(pop):
    cells.append(Cell(random.randint(0, 128), random.randint(0, 128), None, 10))
temp_cells = []

while True:
    display.fill('white')

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if steps_u < steps:
        for cell in cells:
            cell.neuron(pop, 128, 128)
            cell.update(display, 'black', 128, 128)
    else:
        for cell in cells:
            if cell.x < 100:
                temp_cells.append(Cell(random.randint(0, 128), random.randint(0, 128), cell.brain.genome, 0))
        
        cells.clear()
        cells = temp_cells
        temp_cells = []
        steps_u = 0
    steps_u += 1

    screen.blit(pygame.transform.scale(display, (600, 600)), (0, 0))
    pygame.display.update()
    clock.tick(10)
