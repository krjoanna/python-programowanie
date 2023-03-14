# Create the following variables:
# n = 2022
# x = math.pi   # save with 5 digits after a dot (import 'math' first!)
# word = "Python"
# polish = "książka"   # 'book' in English
# Write the variables to a text file "vars.txt",
# one line for one variable.
# Print the file content on the screen.

import math
n = 2022
x = math.pi
word = "Python"
polish = "książka"
varsfile = open("vars.txt",mode = "w", encoding ="utf-8")
varsfile.write("{}\n{}\n{}\n{}".format(n, x, word, polish))  
varsfile.close()

varsfile = open('vars.txt', 'r', encoding ="utf-8")
FileContent = varsfile.read()

print(FileContent)
