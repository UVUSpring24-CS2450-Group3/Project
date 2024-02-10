from uvsim import UVSim
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path to program>")
        return

    fname = sys.argv[1]

    try:
        file = open(fname, "r")
    except FileNotFoundError:
        print(f"Failed to open file '{sys.argv[1]}'")
        return
    
    sim = UVSim()
    with file:
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
            print(f"Successfully loaded program into memory. Executing...")

    sim.run()


if __name__ == "__main__":
    main()
