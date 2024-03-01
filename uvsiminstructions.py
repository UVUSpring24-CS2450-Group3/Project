class UVSimInputCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        succeeded = False
        while not succeeded:
            try:
                value = int(input("Enter a data word: "))
                if value > 9999 or value < -9999:
                    raise ValueError()
                succeeded = True
                self.uvsim.get_memory().write(self.operand, value)
            except ValueError:
                print("Enter a value between -9999 and 9999 (inclusive)\n")

class UVSimOutputCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        print(self.uvsim.get_memory().read(self.operand))

class UVSimLoadCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        self.uvsim.set_acc(self.uvsim.get_memory().read(self.operand))

class UVSimStoreCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        self.uvsim.get_memory().write(self.operand, self.uvsim.get_acc())

class UVSimAddCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        old_acc = self.uvsim.get_acc()
        self.uvsim.set_acc(old_acc + self.uvsim.get_memory().read(self.operand))

class UVSimSubCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        old_acc = self.uvsim.get_acc()
        self.uvsim.set_acc(old_acc - self.uvsim.get_memory().read(self.operand))

class UVSimDivCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        old_acc = self.uvsim.get_acc()
        self.uvsim.set_acc(old_acc / self.uvsim.get_memory().read(self.operand))

class UVSimMulCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        old_acc = self.uvsim.get_acc()
        self.uvsim.set_acc(old_acc * self.uvsim.get_memory().read(self.operand))

class UVSimBranchCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        self.uvsim.pc = self.operand

class UVSimBranchNegCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        if self.uvsim.get_acc() < 0:
            self.uvsim.pc = self.operand

class UVSimBranchZeroCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        if self.uvsim.get_acc() == 0:
            self.uvsim.pc = self.operand

class UVSimHaltCommand:
    def __init__(self, uvsim):
        self.uvsim = uvsim

    def execute(self):
        self.uvsim.running = False
