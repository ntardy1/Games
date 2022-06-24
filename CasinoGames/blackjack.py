
'''
Command terminal is about 200 characters wide (side-to-side) by about 50 characters long (top-to-bottom)
Ratio of Card Height To Width: 1.4:1
Monitor Dimensions: 157 wide, 58 long
'''

# Importing Libraries
from time import sleep
import os
import csv
from pynput.keyboard import Key, Controller
'''
# Establishing variables
data = []

# Extracting the card names from the csv
file = open("carddeck.csv")
csv_read = csv.reader(file)

# Putting all card names into a large lists
# 'Data' is a list of lists: grouped by suit
for element in csv_read:
    data.append(element)
'''
class createCard:
    def __init__(self, number, suit, value):
        self.number = number
        self.suit = suit
        self.value = value

    def displayCard(self):
        cardWidth = 50
        keyboard = Controller()
        if (self.number == "A"):
            keyboard.press("-")
            keyboard.release("-")
            sleep(1)
            #kb.press_and_release('enter')


os.system('cls')
ASpades = createCard('A', 'spades', 11)
ASpades.displayCard()
