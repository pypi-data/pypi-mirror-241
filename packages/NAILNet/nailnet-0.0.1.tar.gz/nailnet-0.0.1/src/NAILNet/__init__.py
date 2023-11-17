import random
import math
import copy

def getMutVal():
    return ((random.random() * 2) - 1) / 10

def chance(percent):
    val = random.random()
    if(percent / 100.0 >= val):
        return True
    return False

def activationCalc(a, val):
    if(a == "linear"):
        return val
    elif(a == "sigmoid"):
        return 1 / (1 + math.exp(-val))
    elif(a == "tanh"):
        return math.tanh(val)
    elif(a == "relu"):
        return max(0, val)
    elif(a == "leaky_relu"):
        if(val >= 0): return val
        return 0.1 * val
    else:
        return None

class Layer():
    def __init__(self, numwpn, numn, activation):
        self.numWeightsPerNode = numwpn
        self.numNodes = numn
        self.weights = []
        self.biases = []
        self.activation = activation

        for i in range(numn):
            self.biases.append(random.random())
            w = []
            for j in range(numwpn):
                w.append(random.random())
            self.weights.append(w)
    
    def calculate(self, inputs):
        if(len(inputs) != self.numWeightsPerNode):
            raise Exception("Input is not of expected length.")
        
        output = []

        for nodeNum in range(self.numNodes):
            weightedSum = 0
            for i in range(len(inputs)):
                weightedSum += self.weights[nodeNum][i] * inputs[i]
            output.append(weightedSum + self.biases[nodeNum])
        return [activationCalc(self.activation, x) for x in output]

    def mutate(self, times):
        for i in range(times):
            self.mutateOnce()

    def mutateOnce(self):
        i = random.randint(0, len(self.weights) - 1)
        j = random.randint(0, len(self.weights[0]) - 1)
        self.weights[i][j] += getMutVal()
        if(chance(0.25)):
            b = random.randint(0, len(self.biases) - 1)
            self.biases[b] += getMutVal()

class Model():
    def __init__(self, lcs, activations, mutpl):
        self.inputSize = lcs[0]
        self.mutpl = mutpl
        self.layers = []
        self.activations = activations
        ac = 0
        pls = lcs[0]
        for lc in lcs[1:]:
            self.layers.append(Layer(pls, lc, activations[ac]))
            pls = lc
            ac += 1

    def evaluate(self, inputs):
        prevVal = inputs
        for layer in self.layers:
            prevVal = layer.calculate(prevVal)
        return prevVal

    def mutate(self, times):
        for i in range(times):
            self.mutateOneLayer()

    def mutateOneLayer(self):
        l = random.randint(0, len(self.layers) - 1)
        self.layers[l].mutate(self.mutpl)

class NEATSim():
    def __init__(self, model_lcs, activations, scoreFunc, populationSize, reproSize, mutSize, mutpl):
        self.mutpl = mutpl
        self.model_lcs = model_lcs
        self.activations = activations
        self.scoreFunc = scoreFunc
        self.popSize = populationSize
        self.reproSize = reproSize
        self.mutSize = mutSize
        self.population = []
        self.generatePop()

    def generatePop(self):
        for i in range(self.popSize):
            self.population.append((0, Model(self.model_lcs, self.activations, self.mutpl)))
        self.calculateFitnesses()

    def sortByFitness(self):
        self.population.sort(reverse=True, key=lambda x: x[0])

    def calculateFitnesses(self):
        for i in range(len(self.population)):
            score = self.scoreFunc(self.population[i][1])
            self.population[i] = (score, self.population[i][1])

    def reproduce(self):
        self.calculateFitnesses()
        self.sortByFitness()
        newPop = self.population[:self.reproSize]
        counter = self.reproSize
        i = 0
        while(counter < self.popSize):
            if(i == self.reproSize): i = 0
            m = copy.deepcopy(newPop[i][1])
            m.mutate(self.mutSize)
            newPop.append((self.scoreFunc(m), m))
            i += 1
            counter += 1
        self.population = newPop

    def simUntilFitnessReached(self, goal):
        gen = 0
        self.sortByFitness()
        while(self.population[0][0] < goal):
            print(f"Gen {gen} highest fitness: {self.population[0][0]} \t| population Size: {len(self.population)}")
            gen += 1
            self.reproduce()
            self.sortByFitness()
        return self.population[0][1]

    def simForRounds(self, rounds):
        self.sortByFitness()
        for r in range(rounds):
            print(f"Round {r} highest fitness: {self.population[0][0]}")
            self.reproduce()
            self.sortByFitness()
        return self.population[0][1]

"""
#example:

scoreModel = lambda x: sum(x.evaluate([1, 2, 3]))

neat = NEATSim([3, 3, 3], ["linear", "linear", "linear"], scoreModel, 100, 15, 5, 5)
model = neat.simUntilFitnessReached(100)
print(scoreModel(model))
"""
