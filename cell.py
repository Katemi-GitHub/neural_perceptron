from perceptron import Neuron_Perceptron
from brain import Brain
from neuron import Neuron
import random

class Cell:
    def __init__(self, x, y, genome = None, n_gen = 0):
        self.genome = genome
        self.x = x
        self.y = y
        self.brain = Brain(self.genome, n_gen)
        self.g_inf = self.brain.get_info()
    
    def border(self, width, height):
        if self.x > width:
            self.x = width - 1
        if self.x < 0:
            self.x = 0
        if self.y > height:
            self.y = height - 1
        if self.y < 0:
            self.y = 0
    
    def mutation(self):
        self.brain.mutation(self.brain.genome)
    
    def neuron(self, pop, bdx, bdy):
        for i, e in enumerate(self.g_inf):
            n = Neuron(e[0], e[1], e[2], e[3], e[4])
            if n.type == 'sensor':
                sensor = Neuron_Perceptron(n.weight)
                if n.id == 'Rnd':
                    guess = sensor.guess(random.randint(-1, 1))
                elif n.id == 'Pop':
                    guess = sensor.guess(pop / 10000)
                elif n.id == 'BDx':
                    guess = sensor.guess(bdx - self.x)
                elif n.id == 'BDy':
                    guess = sensor.guess(bdy - self.y)
            if n.type == 'neutral':
                neutral = Neuron_Perceptron(n.weight)
            if n.sink == 'movement':
                movement = Neuron_Perceptron(n.weight)
                if n.type == 'sensor':
                    output = movement.guess(guess)
                    if n.sink_id == 'Mrn':
                        axys = random.randint(0, 1)
                        if axys == 0:
                            self.x += output
                        else:
                            self.y += output
                    elif n.sink_id == 'MX':
                        self.x += output
                    elif n.sink_id == 'MY':
                        self.y += output

    def reproduce(self, tof):
        if tof == True:
            return self.x, self.y, self.genome, 0

    def update(self, surface, color, width, height):
        self.border(width, height)
        surface.fill(color, ((self.x, self.y), (1,1)))
