import tkinter as tk
from tkinter import ttk

class MorseConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Converter")
        self.root.geometry("600x400")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create and place widgets
        self.input_label = ttk.Label(self.main_frame, text="Enter your message:")
        self.input_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.input_text = tk.Text(self.main_frame, height=4, width=50)
        self.input_text.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        
        self.convert_button = ttk.Button(self.main_frame, text="Convert to Morse", command=self.convert_text)
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))
        
        self.output_label = ttk.Label(self.main_frame, text="Morse Code:")
        self.output_label.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        
        self.output_text = tk.Text(self.main_frame, height=4, width=50, state='disabled')
        self.output_text.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        
        self.clear_button = ttk.Button(self.main_frame, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=5, column=0, columnspan=2)

    def convert_text(self):
        """Convert the input text to Morse code and display it"""
        from main import text_to_morse  # Import here to avoid circular import
        input_message = self.input_text.get("1.0", tk.END).strip()
        morse_result = text_to_morse(input_message)
        
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", morse_result)
        self.output_text.config(state='disabled')

    def clear_fields(self):
        """Clear both input and output fields"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')
