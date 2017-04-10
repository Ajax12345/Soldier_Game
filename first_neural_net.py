import random
from math import e

class Brain:
    def __init__(self):
        self.w = random.randint(-10, 10)
        self.a = 0.01
        self.E = 0.4



    def activation(self, x, y):
        self.summed_input = sum(map(self.summation, x))
        self.output = self.sigma(self.summed_input)
        self.E = self.error(y, self.output)
        self.delta_w(x, self.output, y, self.E)



    def summation(self, x):
        return self.w*x

    def sigma(self, z):
        return 1/(1+e**-z)

    def error(self, target, the_output):
        return 0.5*(target-the_output)**2

    def delta_w(self, the_input, new_output, target, the_error):
        self.the_inputs = sum(map(self.summation, the_input))
        self.w += new_output*(1-new_output)*self.a

        #self.w += self.the_inputs*the_error*(-self.a) #formula: inputs*Error*alpha

    def new_input(self, x):

        self.summed_input = sum(map(self.summation, x))
        self.output = self.sigma(self.summed_input)
        print self.output




the_file = open("prediction_data.txt").readlines()

the_file = [i.strip('\n') for i in the_file]
data_file = [i.split() for i in the_file]

inputs = [map(float, i[:len(i)-1]) for i in data_file]
outputs = [i[len(i)-1] for i in data_file]
outputs = map(int, outputs)





the_brain = Brain()

for i in range(len(inputs)):
    the_brain.activation(inputs[i], outputs[i])

the_brain.new_input([1, 0])
