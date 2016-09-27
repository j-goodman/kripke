import sys

# TERMINAL COMMAND: python kripke.py poe.txt

file_name = sys.argv[1]
with open(file_name) as file:
    input_string = file.read()

output_string = ''

key = {
    'a': 'q',
    'b': 'F',
    'c': 'r',
    'd': 'G',
    'e': ' ',
    'f': 's',
    'g': 'a',
    'h': 'U',
    'i': 't',
    'j': 'b',
    'k': 'u',
    'l': 'H',
    'm': 'c',
    'n': 'Z',
    'o': 'v',
    'p': 'd',
    'q': 'V',
    'r': 'I',
    's': 'w',
    't': 'W',
    'u': 'T',
    'v': 'x',
    'w': 'J',
    'x': 'K',
    'y': 'f',
    'z': 'y',
    'A': 'g',
    'B': 'h',
    'C': 'L',
    'D': 'M',
    'E': 'i',
    'F': 'X',
    'G': 'z',
    'H': 'j',
    'I': 'N',
    'J': 'A',
    'K': 'k',
    'L': 'Y',
    'M': 'B',
    'N': 'l',
    'O': 'O',
    'P': 'P',
    'Q': 'm',
    'R': 'C',
    'S': 'Q',
    'T': 'n',
    'U': 'R',
    'V': 'D',
    'W': 'o',
    'X': 'S',
    'Y': 'E',
    'Z': 'p',
    ' ': 'e',
}

for char in input_string:
    try:
        output_string += key[char]
    except:
        output_string += char

name_length = len(file_name)-4
text_file = open(file_name[:name_length]+"_k.txt", "w")
text_file.write(output_string)
text_file.close()
