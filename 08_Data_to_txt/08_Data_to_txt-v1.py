# checks if something is valid

import re

# Data to be outputted
data = ['I', 'love', 'computers']


has_error ="yes"
while has_error =="yes":
    print()
    filename = input("Enter a filename" )
    has_error="no"

    valid_char = "[A-Za-z0-9]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"

        else:
            problem = ("(no {}'s allowed".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
    else:
        print("You entered a valid filename")

# add .txt suffix!
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()
