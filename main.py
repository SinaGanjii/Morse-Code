from morse_gui import MorseConverterGUI
import tkinter as tk

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

def text_to_morse(text):
    """
    Converts the input text into Morse Code.
    Each letter is converted to its Morse Code representation.
    Spaces in the text are translated to a '/' to indicate a new word.
    Unsupported characters are kept as-is in the output.
    """
    text = text.upper()
    morse_code = []
    
    for char in text:
        if char == ' ':
            morse_code.append('/')
        elif char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(char)

    return ' '.join(morse_code)

def main():
    """Main entry point of the application"""
    root = tk.Tk()
    app = MorseConverterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
