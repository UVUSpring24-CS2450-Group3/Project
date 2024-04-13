import tkinter as tk
from tkinter import filedialog, colorchooser
from tkinter import ttk
from uvsim import UVSim
import os

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
        self.uv_sim.gui_handle = self

        # Load color scheme from config file or use default UVU colors
        self.primary_color = "#4C721D"  # Dark green
        self.off_color = "#FFFFFF"       # White

        self.create_widgets()
        self.master.config(bg=self.primary_color)
        
    def convert_to_six_digit_format(self, filename):
        try:
            new_filename = os.path.splitext(filename)[0] + "_six_digit_format.txt"

            with open(filename, "r") as file:
                lines = file.readlines()

            converted_lines = [f"{int(line.strip()):06}" for line in lines]

            with open(new_filename, "w") as new_file:
                new_file.write("\n".join(converted_lines))

            self.write_output(f"Conversion successful. New file saved as {new_filename}\n")
        except Exception as e:
            self.write_output(f"Conversion failed: {str(e)}\n")


    def write_output(self, line):
        """
        Write output to the output text area.

        Args:
            line (str): The line to be written.
        """
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, line)
        self.output_text.config(state=tk.DISABLED)
        
    def convert_file(self):
        """Prompt the user to select a file for conversion."""
        filename = filedialog.askopenfilename()
        if filename:
            self.convert_to_six_digit_format(filename)

            
    def create_widgets(self):
        """Create GUI widgets."""
        self.input_ready_for_sim = False
        self.sim_needs_input = False
        self.loaded_program = False

        self.tabController = ttk.Notebook(self.master)
        self.tabController.pack(expand=1, fill=tk.BOTH)

        #initialize the tab management lists
        self.tabList = []
        self.output_text_list = []

        # Output display
        self.output_label = tk.Label(self.master,bg=self.primary_color, text="Output:")
        self.output_label.pack()

        self.make_new_file_tab()

        self.tabController.add(self.tabList[0], text='Prog. 1')

        self.button_frame = tk.Frame(self.master, bg=self.primary_color)

        # Input entry
        self.input_label = tk.Label(self.master, bg=self.primary_color, text="Console Input:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self.master, width=50, bg=self.off_color, fg="black")
        self.input_entry.pack()
        self.commit_input_button = tk.Button(self.button_frame, text="Enter", command=self.check_input, bg=self.off_color, fg="black")
        self.commit_input_button.pack()

        # Buttons
        self.load_button = tk.Button(self.button_frame, text="Load Program", command=self.load_program, bg=self.off_color, fg="black")
        self.load_button.pack(side=tk.LEFT)
        self.run_button = tk.Button(self.button_frame, text="Run Program", command=self.run_program, bg=self.off_color, fg="black")
        self.run_button.pack(side=tk.LEFT)
        self.button_frame.pack()

        # Settings button
        self.settings_button = tk.Button(self.master, text="Settings", command=self.open_settings, bg=self.off_color, fg="black")
        self.settings_button.pack()

        self.convert_button = tk.Button(self.button_frame, text="Convert to Six-Digit Format", command=self.convert_file, bg=self.off_color, fg="black")
        self.convert_button.pack(side=tk.LEFT)

        self.open_file_button = tk.Button(self.button_frame, text="Open New File",
                                        command=self.make_new_file_tab, bg=self.off_color, fg="black")
        self.open_file_button.pack(side=tk.LEFT)


    def make_new_file_tab(self):
        self.tabList.append(ttk.Frame(self.tabController))
        tab_count = len(self.tabList) - 1
        self.output_text_list.append(tk.Text(self.tabList[tab_count], height=10, width=50, bg=self.off_color, fg="black"))
        self.output_text_list[tab_count].config(state=tk.DISABLED)
        self.output_text_list[tab_count].pack()

        self.tabController.add(self.tabList[tab_count], text='Prog. ' + str(len(self.tabList)))

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
        self.master.config(bg=self.primary_color)
        self.button_frame.config(bg=self.primary_color)
        self.input_label.config(bg=self.primary_color)
        self.output_label.config(bg=self.primary_color)

        self.load_button.config(bg=self.off_color)
        self.run_button.config(bg=self.off_color)
        self.settings_button.config(bg=self.off_color)
        self.commit_input_button.config(bg=self.off_color)

    def validate_program(self, program):
        if len(program) > 250:
            self.write_output("Error: Program size exceeds maximum allowed size of 250 entries (#00 - #249).\n")
            return False
        return True

    def load_program(self):
        """Load a program from file."""
        #reset the sim when loading a new program into memory
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, "r") as file:
                program_data = file.read()
                
            data_split = program_data.split("\n")

            if self.validate_program(data_split):
                self.open_program_edit_window(program_data)


    def open_program_edit_window(self, program):
        self.program_window = tk.Toplevel(self.master)
        self.program_text = tk.Text(self.program_window)
        self.program_text.insert(tk.END, program)

        self.program_text.pack(expand=True, fill=tk.BOTH)

        self.save_run_button = tk.Button(self.program_window, text="Run Code", command=self.validate_and_run_program)
        self.save_run_button.pack()
        self.save_button = tk.Button(self.program_window, text="Save Code", command=self.save_code)
        self.save_button.pack()
        
    def save_code(self):
        filename = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if filename is None:
            return
        text_to_save = str(self.program_text.get(1.0, tk.END))
        filename.write(text_to_save)
        filename.close()

    def validate_and_run_program(self):
        program_data = self.program_text.get(0.0, "end-1c")
        data_split = program_data.split("\n")
        data = [int(x.strip()) for x in data_split]

        if self.validate_program(data_split):
            self.uv_sim.loadProgram(data)
            self.loaded_program = True
            self.write_output("Program loaded successfully.\n")

            self.program_window.destroy()
            self.uv_sim.start()
            self.run_program()

    def check_input(self):
        if self.sim_needs_input:
            """Enter input for the program."""
            try:
                value = int(self.input_entry.get())
                if value > 9999 or value < -9999:
                    raise ValueError()

                self.input_ready_for_sim = True
                self.run_program()
            except ValueError:
                self.write_output("Enter a value between -9999 and 9999 (inclusive)\n")


        else:
            self.write_output("Program is not yet ready for input!\n")

    def get_output_text(self):
        return self.input_entry.get() if self.input_entry.get() else None

    def clear_output_text(self):
        self.input_entry.delete(0, tk.END)

    def run_program(self):
        if not self.loaded_program:
            self.write_output("Program has not been loaded!\n")
            return
        """Run the loaded program."""

        while self.uv_sim.running:
            output = self.uv_sim.step()
            self.write_output(output)
            if self.sim_needs_input:
                break
