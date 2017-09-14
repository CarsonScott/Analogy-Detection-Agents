from Network import Network
from Factories import RandomNetwork, rr

inputs = 10
layers =  10
sizes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
network = RandomNetwork(inputs, layers, sizes)

x = [rr(100)/100 for i in range(inputs)]
y = network.compute(x)

[print(o) for o in network.output]
