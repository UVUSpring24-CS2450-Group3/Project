
# Class Project for CS-2450
#### UVSim - A Simple Virtual Machine Simulator

### Overview:
UVSim is a simple virtual machine simulator designed to help computer science students learn machine language and computer architecture concepts. It simulates a basic CPU, registers, and main memory, allowing users to execute programs written in BasicML, a simple machine language.


## Installation:

#### Prerequisites:

Python 3.x (https://www.python.org/downloads/)

pytest (https://docs.pytest.org/en/8.0.x/)


#### Installing the Repository
Clone or download the UVSim repository from GitHub: [link_to_repo]
Navigate to the project directory in your terminal or command prompt.

## Usage:

### How to start: 
```
python main.py
```

### How to run tests:
```
pytest tests.py
```

Create a text file containing your BasicML program. Each instruction should occupy one line, with the format: OPCODE OPERAND. For example: 
```
1001
1101
```
#### Execute the program
To load a program, press the "load" button, and navigate to the desired file to be executed

Once the program is loaded, press the "Run" button to begin executing instructions.
You can observe the output of WRITE instructions displayed in the terminal.
Interact with the program (if necessary):

If the program contains READ instructions, the UVSim will prompt you to input values from the keyboard when it encounters those instructions.
Once input is entered into the required textbox, press Run to resume executing instructions

#### Monitor program execution:

The UVSim will continue executing instructions until it encounters a HALT instruction or reaches the end of the program.
BasicML Vocabulary:

## Instructions
### I/O Operations:

#### READ (10): 
Read a word from the keyboard into a specific location in memory.
#### WRITE (11): 
Write a word from a specific location in memory to the screen.

### Load/Store Operations:

#### LOAD (20): 
Load a word from a specific location in memory into the accumulator.
#### STORE (21): 
Store a word from the accumulator into a specific location in memory.

### Arithmetic Operations:

#### ADD (30): 
Add a word from a specific location in memory to the word in the accumulator.
#### SUBTRACT (31): 
Subtract a word from a specific location in memory from the word in the accumulator.
#### DIVIDE (32): 
Divide the word in the accumulator by a word from a specific location in memory.
#### MULTIPLY (33): 
Multiply a word from a specific location in memory by the word in the accumulator.

### Control Operations:

#### BRANCH (40): 
Branch to a specific location in memory.
#### BRANCHNEG (41): 
Branch to a specific location in memory if the accumulator is negative.
#### BRANCHZERO (42): 
Branch to a specific location in memory if the accumulator is zero.
HALT (43): Pause the program.

Using the GUI:
--------------

1. Input Data:
   - Enter a data word in the provided entry field. The data word should be an integer value between -9999 and 9999, inclusive.
   - Click the "Enter" button to input the data into the UVSim memory.

2. Running Programs:
   - Load a program into the UVSim memory using the `Load Program` option.
   - Once a program is loaded, click the "Run Program" button to execute it.
   - The UVSim will step through the program, executing each instruction, and display the output in the text area.

3. Viewing Output:
   - The output of the UVSim program will be displayed in the text area below the input fields.
   - Each line of output corresponds to a debug message or program output generated during execution.
4. Exiting the GUI:
   - To exit the GUI, simply close the window or press the appropriate close button provided by your operating system.

Note: The UVSim GUI provides a convenient interface for interacting with the UVSim, allowing users to input data, run programs, and view output easily. It is designed to be intuitive and user-friendly, making it suitable for both beginners and experienced users.

