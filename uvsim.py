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
		opcode = abs(instr) // 100
		operant = instr % 100
		if instr < 0:
			opcode = -opcode

		memory_loc = instr % 100

		match opcode:
			case 43:
				self.running = False
			case 10:
				value = int(input("input a value"))
				self.memory[operant] = value
			case 11:
				print("Output:" self.memory[operant])
			case 20:
				self.acc = self.memory[operant]
			case 21:
				self.memory[operant] = self.acc
			case 30:
				self.acc += self.memory[operant]
			case 31:
				self.acc -= self.memory[operant]
			case 32:
				self.acc = self.acc / self.memory[operant]
			case 33:
				self.acc = self.acc * self.memory[operant]
			case 40:
				self.pc = operant
			case 41:
				if self.acc < 0:
					self.pc = operant
			case 42:
				if self.acc == 0:
					self.pc = operant
			case 43:
				pass
			

		print(f"{self.pc - 1}: {opcode}, {memory_loc}")
