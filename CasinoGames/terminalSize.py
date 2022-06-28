
# Importing Libraries
import os
from time import sleep
import keyboard

# Clearing the command prompt
os.system('cls')

# Initial variables
dimensions = []
delay = 1
duration = 2
list = []
proceed = True

# Getting the width of the command prompt
while proceed:
    list.append("-")
    str = "".join(list)
    print(f"\r{str}", end='')
    for elem in range(duration * 10):
        if (keyboard.is_pressed('esc')):
            proceed = False
        sleep(delay/(duration * 10))

# Setting the width of the command prompt based on user input
commandPromptWidth = len(list) - 1

# Adding the width to the 'dimensions' list
dimensions.append(commandPromptWidth)

# Resetting variables
os.system('cls')
proceed = True
str = ""
list = []

# Getting the length of the command prompt
while proceed:
    list.append("-\n")
    str = "".join(list)
    os.system('cls')
    print(f"\r{str}", end="")
    for elem in range(duration * 10):
        if (keyboard.is_pressed('esc')):
            proceed = False
        sleep(delay/(duration * 10))

# Setting the length of the command prompt based on user input
commandPromptLength = len(list) - 1

# Adding the length to the 'dimensions' list
dimensions.append(commandPromptLength)

# Printing information
print(f"Command Prompt Width: {commandPromptWidth}\nCommand Prompt Length: {commandPromptLength}")