from Detector import Detector

class Network:

	def __init__(self, inputs, layers, sizes):
		self.layers = []
		self.output = []
		sizes = [inputs]+sizes
		for i in range(layers):
			layer = Detector(sizes[i], sizes[i+1])
			self.layers.append(layer)
			self.output.append([])

	def compute(self, x):
		for i in range(len(self.layers)):
			self.output[i] = self.layers[i].compute(x)
			x = self.output[i]
		return self.output[len(self.output)-1]