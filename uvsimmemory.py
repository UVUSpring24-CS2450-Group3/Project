class UVSimMemory:
    def __init__(self, size):
        self._size = size
        self._memory = [0]*size
    
    def read(self, address) -> int:
        return self._memory[address]
    
    def write(self, address, value):
        self._memory[address] = value

    def get_size(self) -> int:
        return self._size
