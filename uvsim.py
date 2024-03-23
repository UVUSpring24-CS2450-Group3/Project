from uvsimmemory import UVSimMemory
from uvsiminstructions import *

class UVSim:
    def __init__(self, debug=False):
        self.debug = debug
        self.reset()

    def reset(self):
        # Create memory with length 100 words
        self.memory = UVSimMemory(100) 

        # used to verify the presence of input for the GUI
        self.hasInput = False

        # used to inform the GUI that the sim requires input
        self.required_input = False

        # Program counter: track next instruction to execute
        self.pc = 0

        # Accumulator register
        self.acc = 0

        # used to store the input from the GUI as characters
        self.input = ""

        # used to take store the output from the sim so that the
        # gui can access it
        self.output = ""

        if self.debug:
            self.running = True
        else:
            self.running = False
            
    def getmemory(self,address):
        return self.memory.read(address)
    
    def loadProgram(self, data):
        # Verify we can copy all program data into memory
        if len(data) > self.memory.get_size():
            return False

        # Copy all data into memory
        for i in range(len(data)):
            self.memory.write(i, data[i])

        return True

    def get_memory(self):
        return self.memory

    def get_acc(self):
        return self.acc
    
    def set_acc(self, value):
        self.acc = value


    def run(self):
        self.running = True
        while self.running:
            print(self.step())

    def start(self):
        self.running = True

    def step(self):
        self.output = ""
        if not self.running:
            return
        instr = self.memory.read(self.pc)
        self.pc += 1
        opcode = abs(instr) // 100
        operant = instr % 100
        if instr < 0:
            opcode = -opcode

        if self.debug:
            self.output = f"{self.pc - 1}: acc:{self.acc} opc:{opcode}, operand:{operant}\n"

        try:
            command = get_command(opcode, self, operant)
            command.execute()
        except ValueError as e:
            self.output += f"Error: {e}\n"
            self.running = False
            raise e

        return self.output

def get_command(opcode, uvsim, operant):
    if opcode == 10:
        return UVSimInputCommand(uvsim, operant)
    elif opcode == 11:
        return UVSimOutputCommand(uvsim, operant)
    elif opcode == 20:
        return UVSimLoadCommand(uvsim, operant)
    elif opcode == 21:
        return UVSimStoreCommand(uvsim, operant)
    elif opcode == 30:
        return UVSimAddCommand(uvsim, operant)
    elif opcode == 31:
        return UVSimSubCommand(uvsim, operant)
    elif opcode == 32:
        return UVSimDivCommand(uvsim, operant)
    elif opcode == 33:
        return UVSimMulCommand(uvsim, operant)
    elif opcode == 40:
        return UVSimBranchCommand(uvsim, operant)
    elif opcode == 41:
        return UVSimBranchNegCommand(uvsim, operant)
    elif opcode == 42:
        return UVSimBranchZeroCommand(uvsim, operant)
    elif opcode == 43:
        return UVSimHaltCommand(uvsim)
    else:
        raise ValueError(f"Undefined opcode: {opcode}")

