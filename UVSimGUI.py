import tkinter as tk
import uvsim as UVSim

class UVSimGUI:
    def __init__(self, master):
        self.master = master
        self.uv_sim = UVSim(debug=True)  # Initialize UVSim with debug mode

        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self.master, text="Enter a data word:")
        self.input_label.pack()

        self.input_entry = tk.Entry(self.master)
        self.input_entry.pack()

        self.input_button = tk.Button(self.master, text="Enter", command=self.enter_data)
        self.input_button.pack()

        self.output_label = tk.Label(self.master, text="Output:")
        self.output_label.pack()

        self.output_text = tk.Text(self.master, height=10, width=50)
        self.output_text.pack()

        self.run_button = tk.Button(self.master, text="Run Program", command=self.run_program)
        self.run_button.pack()

    def enter_data(self):
        try:
            value = int(self.input_entry.get())
            if value > 9999 or value < -9999:
                raise ValueError()
            self.uv_sim.memory[self.uv_sim.pc] = value
            self.uv_sim.pc += 1
        except ValueError:
            self.output_text.insert(tk.END, "Enter a value between -9999 and 9999 (inclusive)\n")

    def run_program(self):
        self.uv_sim.run()
        self.display_output()

    def display_output(self):
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        for line in self.uv_sim.debug_output:
            self.output_text.insert(tk.END, line + "\n")

