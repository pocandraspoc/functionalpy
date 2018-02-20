class SummableList(list):
	
	def suma(self):
		index = 0
		for vector in self.__iter__():
			index += vector
		return index

m = [1,2,3,4,5,6]
print(SummableList(m).suma())