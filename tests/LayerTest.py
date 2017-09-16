from Layer import Layer
from Factories import RandomLayer

nodes = 5
inputs = 10

samples = [
	[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
]

layer = RandomLayer(inputs, nodes, -50, 100)

log = open("log.txt", "w")
for i in layer.weights:
	for j in i:
		log.write(str(j) + '	')
	log.write('\n')
log.close()
last = ''
this = ''
for i in range(1000000):
	winners = ''
	for s in range(len(samples)):
		output = layer.compute(samples[s])
		layer.update()

		line = str(layer.best) + ')  '

		for k in range(len(output)):
			line += str((output[k])) + ' '
		this += line + '\n'
	
	if last != this:
		print(str(i) + '\n' + this)
	last = this
	this = ''
