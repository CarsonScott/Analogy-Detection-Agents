from Detector import Detector
from Network import Network
from Layer import Layer
from random import randrange as rr

def RandomDetector(inputs, nodes, lower=0, upper=0):
	d = Detector(inputs, nodes)
	for i in range(nodes):
		for j in range(inputs):
			d.biases[i][j] = rr(lower, upper)/100
	return d

def RandomNetwork(inputs, layers, sizes):
	n = Network(inputs, layers, sizes)
	sizes = [inputs]+sizes
	for i in range(layers):
		layer = RandomDetector(sizes[i], sizes[i+1])
		n.layers[i] = layer
	return n

def RandomLayer(inputs, nodes, lower=0, upper=100):
	d = Layer(inputs, nodes)
	for i in range(nodes):
		d.threshold[i] = 2	
		for j in range(inputs):
			d.weights[i][j] = rr(lower, upper)/100
	return d