from Layer import Layer
from Factories import RandomLayer

nodes = 3
inputs = 9

samples = [
	[1, 1, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 1, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 1, 1]
]

layer = RandomLayer(inputs, nodes, -50, 100)

for i in range(100000):
	winners = []
	for s in samples:
		output = layer.compute(s)
		layer.update()

		w = 0
		for i in range(len(output)):
			if output[i] > output[w]: w = i

		winners.append(w)
		if i % 10000: 
			line =''
			for j in range(len(output)):
				line += str(round(output[j]*10000)/10000) + '	'
			print(line + str(w) + "\n")
