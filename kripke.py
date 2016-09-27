import sys

# TERMINAL COMMAND: python kripke.py poe.txt

file_name = sys.argv[1]
suffix = False
try:
    suffix = file_name.split('_k')[1]
    if suffix == '.txt':
        suffix = 'k'
except:
    pass

if suffix == 'k':
    # DECODE:
    with open(file_name) as file:
        input_string = file.read()
    output_string = ''
    x = 0
    y = 7
    while y <= len(input_string):
        chunk = input_string[x:y]
        output_string+=chr(int(chunk, 2))
        x+=7
        y+=7
    name_length = len(file_name)-6
    text_file = open(file_name[:name_length]+".txt", "w")
    text_file.write(output_string)
    text_file.close()
else:
    # ENCODE:
    with open(file_name) as file:
        input_string = file.read()
    output_string = ''
    for char in input_string:
        try:
            charcode = str(bin(ord(char)))
            charcode = charcode.split('b')[1]
            while len(charcode) < 7:
                charcode = '0'+charcode
            output_string += charcode
        except:
            output_string += char

    name_length = len(file_name)-4
    text_file = open(file_name[:name_length]+"_k.txt", "w")
    text_file.write(output_string)
    text_file.close()
