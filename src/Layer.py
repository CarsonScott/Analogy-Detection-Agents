e = 2.718281828459

def logistic(x, a, b, c):
	return a / (1+pow(e,-b*(x-c)))

class Layer:

	def __init__(self, inputs, nodes):
		self.inputs = []
		self.totals = []
		self.outputs = []
		self.weights = []
		self.threshold = []
		self.drate = 0.001
		self.lrate = 0.0001
		self.best = None
	
		for i in range(nodes):
			self.totals.append(0)
			self.threshold.append(0)
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
			self.outputs[i] = logistic(x, 1, 2, self.threshold[i])

		totals = self.totals
		for i in range(len(totals)):	
			dt = 0
			for j in range(len(totals)):
				if i != j: 
					dt += totals[j]
			
			self.totals[i] -= dt*self.drate

		b = None
		for i in range(len(self.outputs)):
			if b == None or self.outputs[i] > self.outputs[b]:
				b = i

		self.best = b
		return self.outputs

	def update(self):
		s = 0
		for i in range(len(self.outputs)):
			o = self.outputs[i]
			s += o

		for i in range(len(self.weights)):
			d = self.outputs[i] 
			if s != 0:
				d /= s
			
			if i == self.best: 
				d *= 1 + 1/len(self.outputs)

			dt = self.totals[i]-self.threshold[i]
			self.threshold[i] += dt*self.lrate

			if self.threshold[i] > 2: 
				self.threshold[i] = 2
			if self.threshold[i] < 0: 
				self.threshold[i] = 0

			for j in range(len(self.weights[i])):
				dw = self.inputs[j]*self.weights[i][j]
				if self.totals[i] != 0: 
					dw /= self.totals[i]

				self.weights[i][j] += d*dw*self.lrate
				if abs(self.weights[i][j]) > 1:
					self.weights[i][j] = self.weights[i][j]/abs(self.weights[i][j]) 