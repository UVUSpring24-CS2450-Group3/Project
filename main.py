from uvsim import UVSim

def main():
    sim = UVSim()
    with open("tests/Test1.txt", "r") as file:
        rawNumbers = file.read().split("\n")
        intNumbers = []
        try:
            for num in rawNumbers:
                intNumbers.append(int(num))
        except:
            print("Failed to parse program data")

        if not sim.loadProgram(intNumbers):
            print("Failed to load program data into simluator")
        else:
            print(f"Loaded program into memory:\n{sim.memory}")

        


if __name__ == "__main__":
    main()
