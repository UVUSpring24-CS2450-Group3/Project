class UVSim:
	def __init__(self):
		self.memory = [0]*100
		self.pc = 0
		self.acc = 0
	
	def loadProgram(self, data):
		if len(data) > len(self.memory):
			return False

		for i in range(len(data)):
			self.memory[i] = data[i]

		return True

	def step(self):
		instr = self.memory[self.pc]
		# parse instruction here