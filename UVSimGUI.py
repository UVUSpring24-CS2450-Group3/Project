import tkinter as tk
from tkinter import filedialog


from uvsim import UVSim

class UVSimGUI:
    def __init__(self, master):
        self.master = master
        self.uv_sim = UVSim(debug=True)  # Initialize UVSim with debug mode

        self.create_widgets()

    def writeOutput(self, line):
        self.output_text.insert(tk.END, line)

    def create_widgets(self):
        # Output display
        self.output_label = tk.Label(self.master, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(self.master, height=10, width=50)
        self.output_text.pack()

        # Input entry
        self.input_label = tk.Label(self.master, text="Console Input:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self.master, width=50)
        self.input_entry.pack()

        # Buttons
        self.button_frame = tk.Frame(self.master)
        self.load_button = tk.Button(self.button_frame, text="Load Program", command=self.load_program)
        self.load_button.pack(side=tk.LEFT)
        self.run_button = tk.Button(self.button_frame, text="Run Program", command=self.run_program)
        self.run_button.pack(side=tk.LEFT)
        self.button_frame.pack()

    def load_program(self):
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, "r") as file:
                raw_numbers = file.readlines()
                try:
                    program = [int(num.strip()) for num in raw_numbers]
                    self.uv_sim.load_program(program)
                    self.write_output("Program loaded successfully.")
                except ValueError:
                    self.write_output("Error: Invalid program format.")
                    
    def create_widgets(self):
        #TODO: organize buttons to match design

        self.output_label = tk.Label(self.master, text="Output:")
        self.output_label.pack()

        self.output_text = tk.Text(self.master, height=10, width=50)
        self.output_text.pack()

        self.input_label = tk.Label(self.master, text="Console Input")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.master, width=50)
        self.input_entry.pack()

        #TODO: allow for usage of the "Enter" key for submitting input
        self.submit_input = tk.Button(self.master, command=self.enter_input)
        self.submit_input.pack()

        self.buttonFrame = tk.Frame(self.master)

        self.file_button = tk.Button(self.buttonFrame, text="Load File", command=self.loadFile)
        self.file_button.pack()

        self.run_button = tk.Button(self.buttonFrame, text="Run Program", command=self.run_program)
        self.run_button.pack()

        self.buttonFrame.pack()

    def enter_input(self):
        try:
            value = int(self.input_entry.get())
            if value > 9999 or value < -9999:
                raise ValueError()
        except ValueError:
            self.output_text.insert(tk.END, "Enter a value between -9999 and 9999 (inclusive)\n")

    def loadFile(self):
        filename = filedialog.askopenfilename()
        with open(filename, "r") as file:
            rawNumbers = file.read().split("\n")
            intNumbers = []
            try:
                for num in rawNumbers:
                    intNumbers.append(int(num))
            except:
                print("Failed to parse program data")
                exit(2)

            if not self.uv_sim.loadProgram(intNumbers):
                print("Failed to load program data into simulator")
                exit(1)

    def run_program(self):
        self.uv_sim.run()
        self.display_output()
    def frankversion_run_program(self):
        console_input = self.input_entry.get().strip()
        if console_input:
            self.uv_sim.set_console_input(console_input)
        self.uv_sim.run()
        self.display_output()


    def display_output(self):
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        for line in self.uv_sim.debug_output:
            self.output_text.insert(tk.END, line + "\n")

