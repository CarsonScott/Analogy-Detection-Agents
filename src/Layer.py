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
		self.lrate = 0.00001
		self.drate = 0.001
		self.best = None
		self.worst = None

	
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
			self.outputs[i] = int(x > self.threshold[i])#logistic(x, 1, 0.5, 2)

#			if self.outputs[i] == 1:
#				if b == None or self.totals[i] > self.totals[b]:
#					b = i
#			if w == None or self.totals[i] < self.totals[w]:
#				w = i
		t = self.totals
		for i in range(len(t)):
			y = 0
			for j in range(len(t)):
				if i != j: y += t[j] 
			self.totals[i] -= y*self.drate

		b = None
		for i in range(len(self.totals)):
			if self.outputs[i]:
				if b == None or self.totals[i] > self.totals[b]:
					b = i

		self.best = b
		return self.outputs

	def update(self):
		s = 0
		for i in range(len(self.outputs)):
			o = self.outputs[i]
			if i == self.best: o *= 1.5
			s += o

		for i in range(len(self.weights)):
			d = self.outputs[i] 
			
			if i == self.best: d *= 1.5
			if s != 0: d /= s


			dt = d*(self.totals[i]-self.threshold[i])
			self.threshold[i] += dt *self.lrate

			if self.threshold[i] < 0: self.threshold[i] = 0
			if self.threshold[i] > 1: self.threshold[i] = 1

			for j in range(len(self.weights[i])):
				dw = self.inputs[j]*self.weights[i][j]
				if self.totals[i] != 0: 
					dw /= self.totals[i]
				self.weights[i][j] += dw * d * self.lrate

				wl = 1
				if abs(self.weights[i][j]) > wl:
					self.weights[i][j] = wl * self.weights[i][j]/abs(self.weights[i][j]) 