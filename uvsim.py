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

	def run(self):
		self.running = True
		while self.running:
			self.step()
	def step(self):
		# Load instruction from memory with program counter
		instr = self.memory[self.pc]
		self.pc += 1

		# parse instruction (it's in base 10)
		opcode = 0
		tmp_instr = instr
		if instr < 0:
			while tmp_instr < -99:
				tmp_instr += 100
				opcode += 1
		else:	
			while tmp_instr > 99:
				tmp_instr -= 100
				opcode += 1

		memory_loc = instr % 100

		match opcode:
			case 43:
				self.running = False
			case _:
				pass

		print(f"{self.pc - 1}: {opcode}, {memory_loc}")