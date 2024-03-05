import tkinter as tk
from tkinter import filedialog

from uvsim import UVSim

class UVSimGUI:
    """A GUI for the UVSim application."""

    def __init__(self, master):
        """
        Initialize the UVSimGUI.

        Args:
            master (tk.Tk): The root window.
        """
        self.master = master
        self.uv_sim = UVSim()

        self.create_widgets()

    def write_output(self, line):
        """
        Write output to the output text area.

        Args:
            line (str): The line to be written.
        """
        self.output_text.insert(tk.END, line)

    def create_widgets(self):
        """Create GUI widgets."""
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
        """Load a program from file."""
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, "r") as file:
                raw_numbers = file.readlines()
                try:
                    program = [int(num.strip()) for num in raw_numbers]
                    self.uv_sim.loadProgram(program)
                    self.write_output("Program loaded successfully.")
                except ValueError:
                    self.write_output("Error: Invalid program format.")

        self.uv_sim.start()

    def enter_input(self):
        """Enter input for the program."""
        try:
            value = int(self.input_entry.get())
            if value > 9999 or value < -9999:
                raise ValueError()
        except ValueError:
            self.output_text.insert(tk.END, "Enter a value between -9999 and 9999 (inclusive)\n")


    def run_program(self):
        """Run the loaded program."""
        if self.uv_sim.required_input:
            self.uv_sim.input = self.input_entry.get()
            self.uv_sim.hasInput = True
            self.uv_sim.required_input = False

        while(self.uv_sim.running):
            output = self.uv_sim.step()
            self.write_output(output)
            if self.uv_sim.required_input:
                break


    def display_output(self):
        """Display the output of the program."""
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        for line in self.uv_sim.debug_output:
            self.output_text.insert(tk.END, line + "\n")
