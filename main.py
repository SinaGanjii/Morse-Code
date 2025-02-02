# Dictionary representing the Morse Code chart
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

def text_to_morse(text):
    """
    Converts the input text into Morse Code.
    Each letter is converted to its Morse Code representation.
    Spaces in the text are translated to a '/' to indicate a new word.
    Unsupported characters are kept as-is in the output.
    """
    # Convert the text to uppercase to match dictionary keys
    text = text.upper()
    morse_code = []
    
    for char in text:
        if char == ' ':
            # Use '/' to separate words in Morse Code
            morse_code.append('/')
        elif char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            # Keep unsupported characters as-is in the output
            morse_code.append(char)

    # Join all Morse code parts with a space for readability
    return ' '.join(morse_code)

def main():
    while True:
        # Ask if user wants to continue or exit
        print("\nEnter 'exit' to quit or any message to convert to Morse Code")
        user_input = input("Enter your message: ")
        
        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Convert the input text to Morse Code
        morse_output = text_to_morse(user_input)
        
        # Display the result
        print("Morse Code:", morse_output)

if __name__ == "__main__":
    main()