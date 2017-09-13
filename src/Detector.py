e = 2.718281828459

class Detector:

	def act(self, x):
		return 1 / (1+pow(e,-1*(x-0)))

	def out(self, n, x):
		s = 0
		for i in range(len(self.biases[n])):
			s += self.biases[n][i] * x[i]
		y = self.act(s)
		return y

	def __init__(self, inputs, nodes):
		self.states = []
		self.output = []
		self.biases = []
		for i in range(nodes):
			self.states.append(1)
			self.output.append(0)
			self.biases.append([])
			for j in range(inputs):
				self.biases[i].append(1)

	def compute(self, x):
		for i in range(len(self.output)):
			out = 0
			if self.states[i]:
				out = self.out(i, x)
			self.output[i] = out
		return self.output

	def winner(self):
		w = 0
		for i in range(len(self.output)):
			if self.output[i] > self.output[w]:
				w = i
		return w