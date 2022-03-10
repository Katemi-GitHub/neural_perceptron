import random
import numpy as np

def sign(data):
    if data >= 0:
        return 1
    else:
        return -1

class Perceptron:
    def __init__(self, w):
        self.trainRate = 0.1
        self.weights = []
        for i in range(w):
            self.weights.append(i)
        i = 0
        while i < len(self.weights):
            self.weights[i] = random.randint(-4, 4)
            i += 1
    
    def guess(self, inputs):
        sum = 0
        i = 0
        while i < len(self.weights):
            sum += inputs[i] * self.weights[i]
            i += 1
        
        output = sign(sum)
        return output
    
    def train(self, inputs, result):
        guess = self.guess(inputs)
        error = result - guess
        i = 0
        while i < len(self.weights):
            self.weights[i] += error * inputs[i] * self.trainRate
            i += 1

class Neuron_Perceptron:
    def __init__(self, weight):
        self.trainRate = 0.1
        self.weight = weight
    
    def guess(self, input):
        return sign(input * self.weight)
    
    def train(self, input, result):
        guess = self.guess(input)
        error = result - guess
        self.weight += error * input * self.trainRate
