class UVSim:
	def __init__(self):
		# Create memory with length 100 words
		self.memory = [0]*100

		# Program counter: track next instruction to execute
		self.pc = 0

		# Accumulator register
		self.acc = 0
	
	def loadProgram(self, data):
		# Verify we can copy all program data into memory
		if len(data) > len(self.memory):
			return False

		# Copy all data into memory
		for i in range(len(data)):
			self.memory[i] = data[i]

		return True

	def step(self):
		# Load instruction from memory with program counter
		instr = self.memory[self.pc]

		# parse instruction here