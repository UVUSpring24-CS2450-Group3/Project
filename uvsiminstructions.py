import time

class UVSimInputCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        """
        CLI MODE
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
        """
        try:
            text = self.uvsim.gui_handle.get_output_text()
            if not self.uvsim.gui_handle.input_ready_for_sim:
                self.uvsim.gui_handle.write_output("Enter a data word: \n")
                self.uvsim.gui_handle.sim_needs_input = True
                self.uvsim.pc -= 1  # Hack to force reexecution of this instruction
            else:
                value = int(text)
                if value > 9999 or value < -9999:
                    raise ValueError()
                self.uvsim.get_memory().write(self.operand, value)
                self.uvsim.gui_handle.write_output("Continuing execution...\n")
                self.uvsim.gui_handle.sim_needs_input = False
                self.uvsim.gui_handle.input_ready_for_sim = False
                self.uvsim.gui_handle.clear_output_text()

        except ValueError:
            self.uvsim.gui_handle.write_output("Enter a value between -9999 and 9999 (inclusive)\n")


class UVSimOutputCommand:
    def __init__(self, uvsim, operand):
        self.uvsim = uvsim
        self.operand = operand

    def execute(self):
        output = self.uvsim.get_memory().read(self.operand)
        self.uvsim.output = f"Output: {output}"
        print(output)
        
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
