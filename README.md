```markdown
# UVSim - A Simple Virtual Machine Simulator

## Overview:
UVSim is a simple virtual machine simulator designed to help computer science students learn machine language and computer architecture concepts. It simulates a basic CPU, registers, and main memory, allowing users to execute programs written in BasicML, a simple machine language.

## Installation:
### Prerequisites:
- Python 3.x ([Download Python](https://www.python.org/downloads/))
- pytest ([pytest Documentation](https://docs.pytest.org/en/8.0.x/))

### Installing the Repository:
1. Clone or download the UVSim repository from GitHub: [link_to_repo]
2. Navigate to the project directory in your terminal or command prompt.

## Usage:
### How to start:
```bash
python main.py
```

### How to run tests:
```bash
pytest tests.py
```

### Using the GUI:
- **Input Data:**
  - Enter a data word in the provided entry field. The data word should be an integer value between -9999 and 9999, inclusive.
  - Click the "Enter" button to input the data into the UVSim memory.

- **Running Programs:**
  - Load a program into the UVSim memory using the Load Program option.
  - Once a program is loaded, click the "Run Program" button to execute it.
  - The UVSim will step through the program, executing each instruction, and display the output in the text area.

- **Viewing Output:**
  - The output of the UVSim program will be displayed in the text area below the input fields.
  - Each line of output corresponds to a debug message or program output generated during execution.

- **Exiting the GUI:**
  - To exit the GUI, simply close the window or press the appropriate close button provided by your operating system.
- **Change Color:
   - Click the "Settings" button to open the color configuration window.
   - Choose primary and off-colors using the provided buttons.
   - The selected color scheme will be applied to the GUI.
- **Input File System:

   - Load a program from a text file using the "Load Program" option.
   - Navigate to the desired file and select it for loading.


## BasicML Vocabulary:
- **Instructions:**
  - **I/O Operations:**
    - `READ (10)`: Read a word from the keyboard into a specific location in memory.
    - `WRITE (11)`: Write a word from a specific location in memory to the screen.
  - **Load/Store Operations:**
    - `LOAD (20)`: Load a word from a specific location in memory into the accumulator.
    - `STORE (21)`: Store a word from the accumulator into a specific location in memory.
  - **Arithmetic Operations:**
    - `ADD (30)`: Add a word from a specific location in memory to the word in the accumulator.
    - `SUBTRACT (31)`: Subtract a word from a specific location in memory from the word in the accumulator.
    - `DIVIDE (32)`: Divide the word in the accumulator by a word from a specific location in memory.
    - `MULTIPLY (33)`: Multiply a word from a specific location in memory by the word in the accumulator.
  - **Control Operations:**
    - `BRANCH (40)`: Branch to a specific location in memory.
    - `BRANCHNEG (41)`: Branch to a specific location in memory if the accumulator is negative.
    - `BRANCHZERO (42)`: Branch to a specific location in memory if the accumulator is zero.
    - `HALT (43)`: Pause the program.
```

Additionally, don't forget to add/update the link to the repository (`[link_to_repo]`).

