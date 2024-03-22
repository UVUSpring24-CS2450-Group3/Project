import tkinter as tk
from tkinter import filedialog, colorchooser
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

        # Load color scheme from config file or use default UVU colors
        self.primary_color = "#4C721D"  # Dark green
        self.off_color = "#FFFFFF"       # White

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
        self.output_text = tk.Text(self.master, height=10, width=50, bg=self.off_color, fg="black")
        self.output_text.pack()

        # Input entry
        self.input_label = tk.Label(self.master, text="Console Input:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self.master, width=50, bg=self.off_color, fg="black")
        self.input_entry.pack()

        # Buttons
        self.button_frame = tk.Frame(self.master)
        self.load_button = tk.Button(self.button_frame, text="Load Program", command=self.load_program, bg=self.primary_color, fg="black")
        self.load_button.pack(side=tk.LEFT)
        self.run_button = tk.Button(self.button_frame, text="Run Program", command=self.run_program, bg=self.primary_color, fg="black")
        self.run_button.pack(side=tk.LEFT)
        self.button_frame.pack()

        # Settings button
        self.settings_button = tk.Button(self.master, text="Settings", command=self.open_settings, bg=self.primary_color, fg="black")
        self.settings_button.pack()

    def open_settings(self):
        """Open settings window for color configuration."""
        settings_window = tk.Toplevel(self.master)
        settings_window.title("Color Settings")

        # Primary color selection
        primary_color_label = tk.Label(settings_window, text="Primary Color:")
        primary_color_label.grid(row=0, column=0)
        primary_color_button = tk.Button(settings_window, text="Choose", command=self.choose_primary_color)
        primary_color_button.grid(row=0, column=1)

        # Off-color selection
        off_color_label = tk.Label(settings_window, text="Off-Color:")
        off_color_label.grid(row=1, column=0)
        off_color_button = tk.Button(settings_window, text="Choose", command=self.choose_off_color)
        off_color_button.grid(row=1, column=1)

    def choose_primary_color(self):
        """Open color chooser for primary color selection."""
        color = colorchooser.askcolor(title="Choose Primary Color", color=self.primary_color)
        if color[1]:  # Check if a color is chosen
            self.primary_color = color[1]
            self.apply_color_scheme()

    def choose_off_color(self):
        """Open color chooser for off-color selection."""
        color = colorchooser.askcolor(title="Choose Off-Color", color=self.off_color)
        if color[1]:  # Check if a color is chosen
            self.off_color = color[1]
            self.apply_color_scheme()

    def apply_color_scheme(self):
        """Apply selected color scheme to GUI."""
        self.output_text.config(bg=self.off_color)
        self.input_entry.config(bg=self.off_color)
        self.load_button.config(bg=self.primary_color)
        self.run_button.config(bg=self.primary_color)
        self.settings_button.config(bg=self.primary_color)

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



