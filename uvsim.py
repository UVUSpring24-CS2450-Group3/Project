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
            
    def getmemory(self,adress):
        return self.memory.read(adress)
    
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
        # Don't allow execution if running = False
        if not self.running:
            return

        # Load instruction from memory with program counter
        instr = self.memory.read(self.pc)
        self.pc += 1

        # parse instruction (it's in base 10)
        opcode = abs(instr) // 100
        operant = instr % 100
        if instr < 0:
            opcode = -opcode

        if self.debug:
            self.output = f"{self.pc - 1}: acc:{self.acc} opc:{opcode}, operand:{operant}\n"

        match opcode:
            case 10:
                #really awkward, but I can't come up with a better way
                #if not self.hasInput:
                #    self.required_input = True
                #    self.pc -= 1
                #    return self.output
                succeeded = False
                while not succeeded:
                    try:
                        #value = int(self.input)
                        value = int(input("Enter a data word: "))
                        if value > 9999 or value < -9999:
                            raise ValueError()
                        succeeded = True
                        self.memory.write(operant, value)
                    except ValueError:
                        print("Enter a value between -9999 and 9999 (inclusive)\n")
                        self.output += "Enter a value between -9999 and 9999 (inclusive)\n"

            case 11:
                self.output += str(self.memory.read(operant))
            case 20:
                self.acc = self.memory.read(operant)
            case 21:
                self.memory.write(operant, self.acc)
            case 30:
                #self.acc += self.memory.read(operant)
                UVSimAddCommand(self, operant).execute()
            case 31:
                UVSimSubCommand(self, operant).execute()
                #self.acc -= self.memory.read(operant)
            case 32:
                UVSimDivCommand(self, operant).execute()
                #self.acc /= self.memory.read(operant)
            case 33:
                UVSimDivCommand(self, operant).execute()
                #self.acc *= self.memory.read(operant)
            case 40:
                self.pc = operant
            case 41:
                if self.acc < 0:
                    self.pc = operant
            case 42:
                if self.acc == 0:
                    self.pc = operant
            case 43:
                self.running = False
            case _:
                self.output += f"Tried to execute undefined opcode {opcode}. Halting..."
                self.running = False
                raise ValueError(f"Tried to execute undefined opcode {opcode}. Halting...")

        return self.output
