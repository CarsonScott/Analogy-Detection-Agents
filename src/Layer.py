e = 2.718281828459

def logistic(x, a, b, c):
	return a / (1+pow(e,-b*(x-c)))

class Layer:

	def __init__(self, inputs, nodes):
		self.inputs = []
		self.totals = []
		self.outputs = []
		self.weights = []
		self.lrate = 0.0001
		self.drate = 0.0001
	
		for i in range(nodes):
			self.totals.append(0)
			self.outputs.append(0)
			self.weights.append([])
			for j in range(inputs):
				self.weights[i].append(1)

	def compute(self, inputs):
		self.inputs = inputs
		for i in range(len(self.weights)):
			x = 0
			for j in range(len(self.weights[i])):
				x += self.inputs[j] * self.weights[i][j]

			self.totals[i] = x
			self.outputs[i] = logistic(x, 1, 2, 0.5)

		o = self.outputs
		for i in range(len(self.outputs)):
			y = 0
			for j in range(len(o)):
				if i != j: y += o[j] * self.lrate 
			self.outputs[i] -= y
		return self.outputs

	def update(self):
		for i in range(len(self.weights)):
			for j in range(len(self.weights[i])):
				dw = self.outputs[i]*self.inputs[i]*self.weights[i][j]/self.totals[i]
				self.weights[i][j] += dw * self.drate

				if abs(self.weights[i][j]):
					self.weights[i][j] /= abs(self.weights[i][j])