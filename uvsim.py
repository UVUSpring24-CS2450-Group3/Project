class UVSim:
    def __init__(self, debug=False):
        self.debug = debug
        self.reset()

    def reset(self):
        # Create memory with length 100 words
        self.memory = [0]*100

        # Program counter: track next instruction to execute
        self.pc = 0

        # Accumulator register
        self.acc = 0

        if self.debug:
            self.running = True
        else:
            self.running = False
    
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
        # Don't allow execution if running = False
        if not self.running:
            return

        # Load instruction from memory with program counter
        instr = self.memory[self.pc]
        self.pc += 1

        # parse instruction (it's in base 10)
        opcode = abs(instr) // 100
        operant = instr % 100
        if instr < 0:
            opcode = -opcode

        if self.debug:
            print(f"{self.pc - 1}: acc:{self.acc} opc:{opcode}, operand:{operant}")


        match opcode:
            case 10:
                succeeded = False
                while not succeeded:
                    try:
                        value = int(input("Enter a data word: "))
                        if value > 9999 or value < -9999:
                            raise ValueError()
                        succeeded = True
                        self.memory[operant] = value
                    except ValueError:
                        print("Enter a value between -9999 and 9999 (inclusive)")
                
            case 11:
                print(self.memory[operant])
            case 20:
                self.acc = self.memory[operant]
            case 21:
                self.memory[operant] = self.acc
            case 30:
                self.acc += self.memory[operant]
            case 31:
                self.acc -= self.memory[operant]
            case 32:
                self.acc /= self.memory[operant]
            case 33:
                self.acc *= self.memory[operant]
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
                print(f"Tried to execute undefined opcode {opcode}. Halting...")
                self.running = False
                raise ValueError(f"Tried to execute undefined opcode {opcode}. Halting...")

