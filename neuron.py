from perceptron import Neuron_Perceptron

sensor_types = ['Rnd', 'Pop', 'BDx', 'BDy']
movement_types = ['Mrn', 'MX', 'MY']

class Neuron:
    def __init__(self, type, id, sink, sink_id, weight):
        temp_id = id
        temp_sid = sink_id
        if type == 0:
            self.type = 'sensor'
            if (temp_id < 32) and (temp_id >= 0):
                self.id = sensor_types[0]
            elif (temp_id < 64) and (temp_id >= 32):
                self.id = sensor_types[1]
            elif (temp_id < 96) and (temp_id >= 64):
                self.id = sensor_types[2]
            elif (temp_id <= 127) and (temp_id >= 96):
                self.id = sensor_types[3]
        else:
            self.type = 'neutral'
        if sink == 0:
            self.sink = 'neutral'
        else:
            self.sink = 'movement'
            if (temp_sid < 43) and (temp_sid >= 0):
                self.sink_id = movement_types[0]
            elif (temp_sid < 86) and (temp_sid >= 43):
                self.sink_id = movement_types[1]
            elif (temp_sid <= 127) and (temp_sid >= 86):
                self.sink_id = movement_types[2]
        self.weight = (weight / 65536) - 32768
    
    def output(self, input):
        neuron = Neuron_Perceptron(self.weight)
        guess = neuron.guess(input)
        return guess
