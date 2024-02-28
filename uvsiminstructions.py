class UVSimAddCommand:
	def __init__(self, sim, operand):
		self.sim = sim
		self.operand = operand

	def execute(self):
		old_acc = self.sim.get_acc()
		self.sim.set_acc(old_acc + self.sim.get_memory().read(self.operand))

class UVSimSubCommand:
	def __init__(self, sim, operand):
		self.sim = sim
		self.operand = operand

	def execute(self):
		old_acc = self.sim.get_acc()
		self.sim.set_acc(old_acc - self.sim.get_memory().read(self.operand))