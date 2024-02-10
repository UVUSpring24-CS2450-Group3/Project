
# Class Project for CS-2450
#### UVSim - A Simple Virtual Machine Simulator

### Overview:
UVSim is a simple virtual machine simulator designed to help computer science students learn machine language and computer architecture concepts. It simulates a basic CPU, registers, and main memory, allowing users to execute programs written in BasicML, a simple machine language.


## Installation:

#### Prerequisites:

Python 3.x (https://www.python.org/downloads/)

#### Installing the Repository
Clone or download the UVSim repository from GitHub: [link_to_repo]
Navigate to the project directory in your terminal or command prompt.

## Usage:

Load a BasicML program into the UVSim:

Create a text file containing your BasicML program. Each instruction should occupy one line, with the format: OPCODE OPERAND. For example: 1001 120.
Run the following command in your terminal: python uvsim.py your_program.txt
Execute the program:

Once the program is loaded, the UVSim will start executing instructions automatically.
You can observe the output of WRITE instructions displayed in the terminal.
Interact with the program (if necessary):

If the program contains READ instructions, the UVSim will prompt you to input values from the keyboard when it encounters those instructions.
Monitor program execution:

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
