from Buffer import Buffer

buffer = Buffer(5)
for i in range(10):
	buffer.add(i)
	print(buffer.get())
	print(buffer.last())