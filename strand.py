import numpy as np

def longest_strand(*filenames):
	files = []
	for filename in filenames:
		with open(filename, 'rb') as file:
			file_bytes = []
			while byte := file.read(1):
				file_bytes.append(byte)
			files.append(np.array(file_bytes))

	def find_strands(files, ):
		# print(files)
		if (sum(files.map(lambda f: len(f) == 0)) < 2):
			return
		
	find_strands({})

filenames = [f'samples/sample.{i}' for i in range(1, 11)]

longest_strand(*filenames)

	