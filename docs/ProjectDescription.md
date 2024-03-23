# UVSim
An important and influential educational client has hired your company to develop a software simulator called UVSim for computer science students to learn machine language and computer architecture. Students can execute their machine language programs on the simulator.

The UVSim is a simple virtual machine, but powerful. The UVSim can only interpret a machine language called BasicML.

The UVSim contains CPU, register, and main memory. An accumulator – a register into which information is put before the UVSim uses it in calculations or examines it in various ways. All the information in the UVSim is handled in terms of words. A word is a signed four-digit decimal number, such as +1234, -5678. The UVSim is equipped with a 100-word memory, and these words are referenced by their location numbers 00, 01, ..., 99. The BasicML program must be loaded into the main memory starting at location 00 before executing. Each instruction written in BasicML occupies one word of the UVSim memory (instruction are signed four-digit decimal number). We shall assume that the sign of a BasicML instruction is always plus, but the sign of a data word may be either plus or minus. Each location in the UVSim memory may contain an instruction, a data value used by a program or an unused area of memory. The first two digits of each BasicML instruction are the operation code specifying the operation to be performed.

BasicML vocabulary defined as follows:

I/O operation:
READ = 10 Read a word from the keyboard into a specific location in memory.
WRITE = 11 Write a word from a specific location in memory to screen.

Load/store operations:
LOAD = 20 Load a word from a specific location in memory into the accumulator.
STORE = 21 Store a word from the accumulator into a specific location in memory.

Arithmetic operation:
ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

Control operation:
BRANCH = 40 Branch to a specific location in memory
BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative.
BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero.
HALT = 43 Pause the program

The last two digits of a BasicML instruction are the operand – the address of the memory location containing the word to which the operation applies.

What you'll be submitting:

Design Document (20 pts) -- document that describes the high-level functionality of your application.  Your document will need at least 2 User Stories and 10-15 use cases outlining the functionality of your application.  (Ranges here are deliberate to avoid making your use cases too broad or too narrow.)

Working Prototype  (40 pts) -- prototype of your application that works from the command line -- it should ask for an input file and then process that file (using the console for any input/output specified by the file contents itself).  This is a prototype, so code it with an eye towards getting it working first, but also with an eye towards (as yet unknown) future expansion.  ALL team members must contribute to the code base -- you will need to submit a link to your source control base (or a screenshot from your source control that shows that all team members have checked in code for your project).

Unit Tests (30 pts) -- each use case should have two unit tests (so 20-30 total) to test the functionality of each use case (you can have more if you deem it suitable for that use case -- remember that unit tests in general need to test both the success condition(s) for each function as well as all possible failure conditions as well.).   The code for the unit tests should also be part of your source control code base.     You will also create a spreadsheet that lists the unit tests in row/column form.  Give each unit test a name, short description, the reference to the appropriate use case, inputs, expected outputs, and how you know whether the test succeeded or failed.

Other Documents (10 pts) -- Create a README.txt text file that describes how to use your application from the command line.  The grader should not need any information outside of your README to understand how to launch and use your application.  Make sure you note here if the programming language you used for the project requires some prerequisites to be installed ahead of time in order for your project to run. In addition to README, also submit your meeting reports from this sprint.