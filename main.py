'''
    Program: Calculator !
    Author: Kasra Naderi
    Copyright: 2020
'''

import re

print("Fully functional python calculator !")
print("type 'quit' to exit.")

previous = 0
run = True


def doMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Please enter your equation: ")
    else:
        print(previous)
        equation = input(str(previous))

    if equation == 'quit':
        print("Have a nice day !")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.(): ]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    doMath()
