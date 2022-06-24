
'''
Command terminal is about 200 characters wide (side-to-side) by about 50 characters long (top-to-bottom)
Ratio of Card Height To Width: 1.4:1
Monitor Dimensions: 157 wide, 58 long
'''

# Importing Libraries
from time import sleep
import os
import csv

# Variables
data = []
terminalWidth = 157 # user dependent
terminalLength = 58 # user dependent
cardWidth = round(terminalWidth/5.81481)
cardHeight = round(terminalLength/3.2222)
masterList = []
rowList = []

# Extracting the card names from the csv
file = open("carddeck.csv")
csv_read = csv.reader(file)

# Putting all card names into a large lists
# 'Data' is a list of lists: grouped by suit
for element in csv_read:
    data.append(element)

def updateScreen(masterList):
    os.system('cls')
    for row in range(terminalLength):
        if (row == 0):
            gameBoard = "".join(masterList[row])
        else:
            gameBoard = gameBoard + "".join(masterList[row])
    print(gameBoard)
def drawCard(cardSide, cardTop):
    for num in range(cardWidth):
        masterList[cardTop][num + cardSide + 1] = "-"
        masterList[cardTop + cardHeight + 1][num + cardSide + 1] = "-"
    for num in range(cardHeight):
        masterList[num + cardTop + 1][cardSide] = "|"
        masterList[num + cardTop + 1][cardSide + cardWidth + 1] = "|"
class createCard:
    def __init__(self, number, suit, value):
        self.number = number
        self.suit = suit
        self.value = value
        if (self.suit == "Diamonds"):
            self.suit = "\u2666"
        elif (self.suit == "Hearts"):
            self.suit = "\u2665"
        elif (self.suit == "Spades"):
            self.suit = "\u2660"
        elif (self.suit == "Clubs"):
            self.suit = "\u2663"
    def displayCard(self, position):
        # Card left offset
        cardSideInitial = round(terminalWidth/52.3333)
        bottomCardTop = round(terminalLength/2.32)
        topCardTop = round(terminalLength/58)
        horizontalCardSpacing = round(terminalWidth/39.25)
        # Player first card
        if (position == 0):
            # Card frame
            cardSide = cardSideInitial
            cardTop = bottomCardTop
            drawCard(cardSide, cardTop)
            # Drawing Suit, Denotation
            masterList[bottomCardTop + 2][cardSideInitial + 3] = self.number
            masterList[bottomCardTop + cardHeight - 1][cardSideInitial + cardWidth - 2] = self.number
            masterList[bottomCardTop + round(cardHeight/2)][cardSideInitial + round(cardWidth/2)] = self.suit
        # Player second card
        elif (position == 1):
            # Card frame
            cardSide = horizontalCardSpacing + cardWidth + cardSideInitial
            cardTop = bottomCardTop
            drawCard(cardSide, cardTop)
            # Drawing Suit, Denotation
            masterList[bottomCardTop + 2][cardSideInitial + horizontalCardSpacing + cardWidth + 3] = self.number
            masterList[bottomCardTop + cardHeight - 1][horizontalCardSpacing + (2 * cardWidth) + cardSideInitial - 2] = self.number
            masterList[bottomCardTop + round(cardHeight/2)][cardSideInitial + round(3 * cardWidth/2) + horizontalCardSpacing + 1] = self.suit
        # Player third card
        elif (position == 2):
            # Card frame
            cardSide = (2 * horizontalCardSpacing) + (2 * cardWidth) + cardSideInitial
            cardTop = bottomCardTop
            drawCard(cardSide, cardTop)
            # Drawing Suit, Denotation
            masterList[bottomCardTop + 2][(2 * horizontalCardSpacing) + (2 * cardWidth) + cardSideInitial + 3] = self.number
            masterList[bottomCardTop + cardHeight - 1][(2 * horizontalCardSpacing) + (3 * cardWidth) + cardSideInitial - 2] = self.number
            masterList[bottomCardTop + round(cardHeight/2)][cardSideInitial + round(5 * cardWidth/2) + (2 * horizontalCardSpacing)] = self.suit
        # Dealer first card
        elif (position == 3):
            # Card frame
            cardSide = cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Suit, Denotation
            masterList[topCardTop + 2][cardSideInitial + 3] = self.number
            masterList[topCardTop + cardHeight - 1][cardSideInitial + cardWidth - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + round(cardWidth/2)] = self.suit
        # Dealer second card
        elif (position == 4):
            # Card frame
            cardSide = horizontalCardSpacing + cardWidth + cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Suit, Denotation
            masterList[topCardTop + 2][cardSideInitial + horizontalCardSpacing + cardWidth + 3] = self.number
            masterList[topCardTop + cardHeight - 1][cardSideInitial + (2 * cardWidth) + horizontalCardSpacing - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + horizontalCardSpacing + round(3 * cardWidth/2) + 1] = self.suit
        # Dealer third card
        elif (position == 5):
            # Card frame
            cardSide = (2 * horizontalCardSpacing) + (2 * cardWidth) + cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Suit, Denotation
            masterList[topCardTop + 2][(2 * horizontalCardSpacing) + (2 * cardWidth) + cardSideInitial + 3] = self.number
            masterList[topCardTop + cardHeight - 1][(2 * horizontalCardSpacing) + (3 * cardWidth) + cardSideInitial - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + (2 * horizontalCardSpacing) + round(5 * cardWidth/2)] = self.suit
        # Dealer fourth card
        elif (position == 6):
            # Card frame
            cardSide = (3 * horizontalCardSpacing) + (3 * cardWidth) + cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Suit, Denotation
            masterList[topCardTop + 2][cardSideInitial + (3 * horizontalCardSpacing) + (3 * cardWidth) + 3] = self.number
            masterList[topCardTop + cardHeight - 1][cardSideInitial + (3 * horizontalCardSpacing) +  (4 * cardWidth) - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + round(7 * cardWidth/2) + (3 * horizontalCardSpacing) + 1] = self.suit
        # Dealer fifth card
        elif (position == 7):
            # Card frame
            cardSide = (4 * horizontalCardSpacing) + (4 * cardWidth) + cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Suit, Denotation
            masterList[topCardTop + 2][cardSideInitial + (4 * horizontalCardSpacing) + (4 * cardWidth) + 3] = self.number
            masterList[topCardTop + cardHeight - 1][cardSideInitial + (4 * horizontalCardSpacing) +  (5 * cardWidth) - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + round(9 * cardWidth/2) + (4 * horizontalCardSpacing)] = self.suit
        updateScreen(masterList)

os.system('cls')

for column in range(terminalWidth):
    rowList.append(" ")
rowList.append("\n")
for row in range(terminalLength):
    masterList.append(list(rowList))

ASpades = createCard("T", 'Spades', 11)
ASpades.displayCard(3)
ASpades.displayCard(0)
ASpades.displayCard(1)
ASpades.displayCard(2)
ASpades.displayCard(4)
ASpades.displayCard(5)
ASpades.displayCard(6)
ASpades.displayCard(7)
