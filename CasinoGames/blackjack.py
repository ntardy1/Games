
# Importing Libraries
from time import sleep
from random import randint
import os
import csv

# Game Display Variables
# Using python os package to get terminal window dimensions
terminalWidth = os.get_terminal_size()[0]
# Subtracting 6 to leave room for player input and text output at the end of each hand
terminalLength = os.get_terminal_size()[1] - 6
cardWidth = round(terminalWidth/5.81481)
cardHeight = round(terminalLength/3.2222)
cardSideInitial = round(terminalWidth/52.3333)
bottomCardTop = round(terminalLength/2.32)
topCardTop = round(terminalLength/58)
horizontalCardSpacing = round(terminalWidth/39.25)
masterList = []
rowList = []

# Player Information Variables
namesList = []

# Making a list to hold the deck(s) of cards
cardDeck = []
dealerCards = []

# Extracting the card names from the csv
cardFile = open(r"cardDeck.csv", "r")
csv_Cards = csv.reader(cardFile)

# Reading the player names from the csv
namesFile = open(r"swissBank.csv", "r", newline="")
csv_Names = csv.reader(namesFile)
# Adding names that are in database (swissBank.csv) to namesList
for elem in csv_Names:
    namesList.append(elem)
# Reopening the swissBank.csv file in append mode
namesFile = open(r"swissBank.csv", "a+", newline="")
# Putting all card names into a large list
for element in csv_Cards:
    cardDeck.append(element)
cardDeck = cardDeck[0]

# Card Related Functions
def refillShoe(deckCount):
    # Extracting the card names from the csv
    cardFile = open(r"cardDeck.csv", "r")
    csv_Cards = csv.reader(cardFile)        
    # Resetting the card deck list
    cardDeck = []
    # Filling it with one deck
    for element in csv_Cards:
        cardDeck.append(element)
    cardDeck = cardDeck[0]
    # Adding every additional deck (if called for)
    for num in range(deckCount - 1):
        for index in range(52):
            cardDeck.append(cardDeck[index])
    return cardDeck
# Randoming drawing a new card from the deck
def newCard():
    # Generate a random number to be used as an index
    randomNumber1 = randint(0, len(cardDeck) - 1)
    card = cardDeck[randomNumber1]
    # Create a new card for the hand based on its number
    if (any(card[0] == str(num) for num in range(2, 10))):
        chosenCard = createCard(card[0], card[1], int(card[0]))
    elif (card[0] == "A"):
        chosenCard = createCard(card[0], card[1], 11)
    else:
        chosenCard = createCard(card[0], card[1], 10)
    # Remove the card to avoid repetition errors
    cardDeck.remove(card)
    return chosenCard

# GUI Related Functions
# Print the masterList, in its current state, as a string
def updateScreen(masterList):
    # Clear the screen
    os.system('cls')
    # Turn the entire masterList into one long string
    # with strategically-placed \n's
    for row in range(terminalLength):
        if (row == 0):
            gameBoard = "".join(masterList[row])
        else:
            gameBoard = gameBoard + "".join(masterList[row])
    # Print the previously mentioned string
    print(gameBoard)
# Reset the masterList to be a list of the same length,
# but with " " as every element (except for select \n's)
def resetMasterList(rowList, masterList):
    if (len(rowList) == 0):
        for column in range(terminalWidth):
            rowList.append(" ")
        rowList.append("\n")
    if (len(masterList) == 0):
        for row in range(terminalLength):
            masterList.append(list(rowList))
    else:
        for row in range(terminalLength):
            for column in range(terminalWidth):
                if (masterList[row][column] != "\n"):
                    masterList[row][column] = " "
    return(masterList)
# Use starting points (character spots) to draw the frame of a card in the terminal window
def drawCard(cardSide, cardTop):
    for num in range(cardWidth):
        masterList[cardTop][num + cardSide + 1] = "-"
        masterList[cardTop + cardHeight + 1][num + cardSide + 1] = "-"
    for num in range(cardHeight):
        masterList[num + cardTop + 1][cardSide] = "|"
        masterList[num + cardTop + 1][cardSide + cardWidth + 1] = "|"
# This is used in the case of splitting
# It redraws the cards that are being "partially covered"
def redrawCard(position):
    # Player first card
    if (position == 0):
        # Dimensions of the left-most player card
        cardSide = cardSideInitial
        cardTop = bottomCardTop
        # "Erasing" the bottom corner card number
        masterList[bottomCardTop + cardHeight - 1][cardSideInitial + cardWidth - 2] = " "
        for num in range(round(cardWidth/2) + 1, cardWidth + 1):
            masterList[cardTop + cardHeight + 1][num + cardSide + 1] = " "
        for num in range(round(cardHeight/2) + 1, cardHeight):
            masterList[cardTop + num + 1][cardSide + cardWidth + 1] = " "
        updateScreen(masterList)
        # Dimensions of the (actual) second player card
        cardSide = horizontalCardSpacing + cardWidth + cardSideInitial
        cardTop = bottomCardTop
        # "Erasing" the bottom left corner of the (actual) second player card
        for num in range(round(cardWidth/2) - horizontalCardSpacing + 1):
            masterList[cardTop + cardHeight + 1][num + cardSide + 1] = " "
        for num in range(round(cardHeight/2) + 1, cardHeight):
            masterList[cardTop + num + 1][cardSide] = " "
        updateScreen(masterList)
    # Player second card
    elif (position == 1):
        # Dimensions of the (actual) second player card
        cardSide = horizontalCardSpacing + cardWidth + cardSideInitial
        cardTop = bottomCardTop
        # "Erasing" the bottom corner card number
        masterList[bottomCardTop + cardHeight - 1][horizontalCardSpacing + (2 * cardWidth) + cardSideInitial - 2] = " "
        # "Erasing" the bottom right corner of the (actual) second player card
        for num in range(round(cardWidth/2) + 1, cardWidth):
            masterList[cardTop + cardHeight + 1][num + cardSide + 1] = " "
        for num in range(round(cardHeight/2) + 1, cardHeight):
            masterList[cardTop + num + 1][cardSide + cardWidth + 1] = " "
        updateScreen(masterList)
# This is a function that would draw a "poker chip" on the terminal window
# with the current wager displayed at the center of the chip
# It is not currently called anywhere (and doesn't really work yet)
def drawChip(wager):
    center = cardSideInitial + round(7 * cardWidth/2) + round(3 * horizontalCardSpacing)
    radius = round(cardWidth/2)
    masterList[bottomCardTop + round(cardHeight/2) - radius][center] = "@"
    masterList[bottomCardTop + round(cardHeight/2) + radius][center] = "@"
    for num in range(radius):
        masterList[bottomCardTop + round(cardHeight/2) + num - radius][center - num] = "@"
        masterList[bottomCardTop + round(cardHeight/2) + num - radius][center + num] = "@"
    for num in range(radius):
        masterList[bottomCardTop + round(cardHeight/2) - num + radius][center - num] = "@"
        masterList[bottomCardTop + round(cardHeight/2) - num + radius][center + num] = "@"
    masterList[bottomCardTop + round(cardHeight/2)][center] = f"{playerWager}"

# Money Related Functions
def swissBank(player):
    # The bank screen is completely independent of the game screen,
    # so start by clearing the screen
    os.system('cls')
    spacer = []
    # This loop and the "headerSpacing" variable are used to center
    # the "Swiss Bank" test at the top of the screen
    for num in range(round(terminalWidth/2) - 5):
        spacer.append(" ")
    headerSpacing = "".join(spacer)
    # Print the "Swiss Bank" screen
    updateBankScreen(headerSpacing)
    # Get the player's desired action
    choice = input("Deposit (d), Withdraw (w), Exit(e): ")
    # Make sure the input is valid
    while (choice != "d" and choice !=  "w" and choice != "e"):
        updateBankScreen(headerSpacing)
        choice = input("Invalid choice\nDeposit (d), Withdraw (w), Exit(e): ")
    while (choice != "e"):
        # Depositing money into account
        if (choice == "d"):
            deposit = int(input("Enter Amount to Deposit: "))
            player.account += deposit
            player.money -= deposit
            updateBankScreen(headerSpacing)
        # Withdrawing money from account
        elif (choice == "w"):
            withdrawn = int(input("Enter Amount to Withdraw: "))
            player.account -= withdrawn
            player.money += withdrawn
            updateBankScreen(headerSpacing)
        choice = input("Deposit (d), withdraw (w), Exit(e): ")
        # Making sure the input is valid
        while (choice != "d" and choice !=  "w" and choice != "e"):
            updateBankScreen(headerSpacing)
            choice = input("Invalid choice\nDeposit (d), Withdraw (w), Exit(e): ")
    # Returning to the game screen if the player chooses
    # to "leave" the bank
    updateScreen(masterList)
# Clears the screen and prints the appropriate information
def updateBankScreen(headerSpacing):
    os.system('cls')
    print(f"\n{headerSpacing}Swiss Bank{headerSpacing}")
    print(f"\nPatron: {playerName}")
    print(f"Account Balance: {player.account}")
    print(f"Money Currently Withdrawn: {player.money}")
    print("\nWhat would you like to do?")
# Handles all logic and money distribution related to the "final showdown"
def finalShowdown(position, player, dealerSum):
    while True:
        # The player has busted
        if (player.sum > 21 and all(card.value != 11 for card in player.cards)):
            mainPlayer.money -= player.wager
            print(f"Dealer wins")
            break
        # The player is above 21 and has an Ace to bring down
        elif (player.sum > 21 and any(card.value == 11 for card in player.cards)):
            for card in player.cards:
                if (card.number == "A" and card.value == 11):
                    card.value = 1
                    player.sum -= 10
                    break
        # The dealer has busted
        elif (dealerSum > 21 and all(card.value != 11 for card in dealerCards)):
            mainPlayer.money += player.possibleGain
            print(f"Player wins")
            break
        # The dealer is above 21 and has an Ace to bring down
        elif (dealerSum > 21 and any(card.value == 11 for card in dealerCards)):
            for card in dealerCards:
                if (card.number == "A" and card.value == 11):
                    card.value = 1
                    dealerSum -= 10
                    break
        # The dealer has not busted and has used all five card slots
        elif (dealerSum >= 17 and dealerSum <= 21 and player.sum > dealerSum and len(dealerCards) == 5):
            chosenCard = newCard()
            chosenCard.displayCard(7)
            dealerSum += chosenCard.value
            dealerCards.append(chosenCard)
        # The dealerSum is less than 17 and all 5 card slots are full
        elif (dealerSum < 17 and len(dealerCards) == 5):
            chosenCard = newCard()
            chosenCard.displayCard(7)
            dealerSum += chosenCard.value
            dealerCards.append(chosenCard)
        # The dealer has beat the player and is in [17, 21]
        elif (dealerSum >= 17 and dealerSum > player.sum and dealerSum <= 21):
            mainPlayer.money -= player.wager
            print(f"Dealer wins")
            break
        elif (dealerSum >= 17 and dealerSum <= 21 and player.sum > dealerSum):
            chosenCard = newCard()
            chosenCard.displayCard(position)
            position += 1
            dealerSum += chosenCard.value
            dealerCards.append(chosenCard)
        # The dealer is below 17
        elif (dealerSum < 17):
            chosenCard = newCard()
            chosenCard.displayCard(position)
            position += 1
            dealerSum += chosenCard.value
            dealerCards.append(chosenCard)
        elif (player.sum == dealerSum):
            print(f"Tie")
            break
        sleep(2)
    # Erasing the list of mainPlayer.cards
    while (len(mainPlayer.cards) != 0):
        mainPlayer.cards.remove(mainPlayer.cards[0])
    # Resetting the masterList
    resetMasterList(rowList, masterList)
    # Updating the playerMoney variable for continuity purposes
    playerMoney = mainPlayer.money
    return position, playerMoney, dealerSum

# Class for Card Defintions
class createCard:
    def __init__(self, number, suit, value):
        self.number = number
        self.suit = suit
        self.value = value
        # Suit == Diamonds
        if (self.suit == "D"):
            self.suit = "\u2666"
        # Suit == Hearts
        elif (self.suit == "H"):
            self.suit = "\u2665"
        # Suit == Spades
        elif (self.suit == "S"):
            self.suit = "\u2660"
        # Suit == Clubs
        elif (self.suit == "C"):
            self.suit = "\u2663"
    # Function to display a card in the terminal window
    def displayCard(self, position):
        # Player first card
        if (position == 0):
            # Card frame
            cardSide = cardSideInitial
            cardTop = bottomCardTop
            drawCard(cardSide, cardTop)
            # Drawing Denotation, Suit
            masterList[bottomCardTop + 2][cardSideInitial + 3] = self.number
            masterList[bottomCardTop + cardHeight - 1][cardSideInitial + cardWidth - 2] = self.number
            masterList[bottomCardTop + round(cardHeight/2)][cardSideInitial + round(cardWidth/2)] = self.suit
        # Player second card
        elif (position == 1):
            # Card frame
            cardSide = horizontalCardSpacing + cardWidth + cardSideInitial
            cardTop = bottomCardTop
            drawCard(cardSide, cardTop)
            # Drawing Denotation, Suit
            masterList[bottomCardTop + 2][cardSideInitial + horizontalCardSpacing + cardWidth + 3] = self.number
            masterList[bottomCardTop + cardHeight - 1][horizontalCardSpacing + (2 * cardWidth) + cardSideInitial - 2] = self.number
            masterList[bottomCardTop + round(cardHeight/2)][cardSideInitial + round(3 * cardWidth/2) + horizontalCardSpacing + 1] = self.suit
        # Player third card
        elif (position == 2):
            # Card frame
            cardSide = (2 * horizontalCardSpacing) + (2 * cardWidth) + cardSideInitial
            cardTop = bottomCardTop
            drawCard(cardSide, cardTop)
            # Drawing Denotation, Suit
            masterList[bottomCardTop + 2][(2 * horizontalCardSpacing) + (2 * cardWidth) + cardSideInitial + 3] = self.number
            masterList[bottomCardTop + cardHeight - 1][(2 * horizontalCardSpacing) + (3 * cardWidth) + cardSideInitial - 2] = self.number
            masterList[bottomCardTop + round(cardHeight/2)][cardSideInitial + round(5 * cardWidth/2) + (2 * horizontalCardSpacing)] = self.suit
        # Dealer first card
        elif (position == 3):
            # Card frame
            cardSide = cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Denotation, Suit
            masterList[topCardTop + 2][cardSideInitial + 3] = self.number
            masterList[topCardTop + cardHeight - 1][cardSideInitial + cardWidth - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + round(cardWidth/2)] = self.suit
        # Dealer second card
        elif (position == 4):
            # Card frame
            cardSide = horizontalCardSpacing + cardWidth + cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Denotation, Suit
            masterList[topCardTop + 2][cardSideInitial + horizontalCardSpacing + cardWidth + 3] = self.number
            masterList[topCardTop + cardHeight - 1][cardSideInitial + (2 * cardWidth) + horizontalCardSpacing - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + horizontalCardSpacing + round(3 * cardWidth/2) + 1] = self.suit
        # Dealer third card
        elif (position == 5):
            # Card frame
            cardSide = (2 * horizontalCardSpacing) + (2 * cardWidth) + cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Denotation, Suit
            masterList[topCardTop + 2][(2 * horizontalCardSpacing) + (2 * cardWidth) + cardSideInitial + 3] = self.number
            masterList[topCardTop + cardHeight - 1][(2 * horizontalCardSpacing) + (3 * cardWidth) + cardSideInitial - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + (2 * horizontalCardSpacing) + round(5 * cardWidth/2)] = self.suit
        # Dealer fourth card
        elif (position == 6):
            # Card frame
            cardSide = (3 * horizontalCardSpacing) + (3 * cardWidth) + cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Denotation, Suit
            masterList[topCardTop + 2][cardSideInitial + (3 * horizontalCardSpacing) + (3 * cardWidth) + 3] = self.number
            masterList[topCardTop + cardHeight - 1][cardSideInitial + (3 * horizontalCardSpacing) +  (4 * cardWidth) - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + round(7 * cardWidth/2) + (3 * horizontalCardSpacing) + 1] = self.suit
        # Dealer fifth card
        elif (position == 7):
            # Card frame
            cardSide = (4 * horizontalCardSpacing) + (4 * cardWidth) + cardSideInitial
            cardTop = topCardTop
            drawCard(cardSide, cardTop)
            # Drawing Denotation, Suit
            masterList[topCardTop + 2][cardSideInitial + (4 * horizontalCardSpacing) + (4 * cardWidth) + 3] = self.number
            masterList[topCardTop + cardHeight - 1][cardSideInitial + (4 * horizontalCardSpacing) +  (5 * cardWidth) - 2] = self.number
            masterList[topCardTop + round(cardHeight/2)][cardSideInitial + round(9 * cardWidth/2) + (4 * horizontalCardSpacing)] = self.suit
        # Split: First hand, second card
        elif (position == 8):
            # Card frame
            cardSide = cardSideInitial + round(cardWidth/2) + 1
            cardTop = bottomCardTop + round(cardHeight/2) + 1
            drawCard(cardSide, cardTop)
            redrawCard(0)
            # Drawing Denotation, Suit
            masterList[cardTop + 2][cardSide + 2] = self.number
            masterList[cardTop + cardHeight - 2][cardSide + cardWidth - 2] = self.number
            masterList[cardTop + round(cardHeight/2)][cardSide + round(cardWidth/2)] = self.suit
        # Split: Second hand, second card
        elif (position == 9):
            # Card frame
            cardSide = cardSideInitial + horizontalCardSpacing + round(3 * cardWidth/2) + 2
            cardTop = bottomCardTop + round(cardHeight/2) + 1
            drawCard(cardSide, cardTop)
            redrawCard(1)
            # Drawing Denotation, Suit
            masterList[cardTop + 2][cardSide + 2] = self.number
            masterList[cardTop + cardHeight - 2][cardSide + cardWidth - 2] = self.number
            masterList[cardTop + round(cardHeight/2)][cardSide + round(cardWidth/2)] = self.suit
        updateScreen(masterList)

# Class for Player(s)
class createPlayer:
    def __init__(self, sum, cards, wager, money, account):
        self.sum = sum
        self.cards = cards
        # The amount of money that will be placed on each individual hand
        self.wager = wager
        # The amount of money that the player could win (based on wager amount)
        # Most sources indicate that Blackjack pays 3:2
        self.possibleGain = round(3 * wager/2)
        self.money = money
        self.account = account

# Clearing the screen at the beginning of the game
os.system('cls')

# Emptying the masterList
resetMasterList(rowList, masterList)

# Getting player name
playerName = input("Player Name: ")
# Checking to see if existing player
for index in range(1, len(namesList)):
    # The database name is the same as the entered name
    if (namesList[index][0] == playerName):
        # Saving the index for csv writing reasons
        playerIndex = index
        playerAccount = int(namesList[playerIndex][2])
        playerMoney = int(namesList[playerIndex][3])
        passwordAttempt = input("Password: ")
        # Making the player enter the correct password in order to log in
        while passwordAttempt != namesList[playerIndex][1]:
            os.system('cls')
            print(f"Player: {playerName}")
            passwordAttempt = input("Password incorrect\nTry again: ")
        os.system("cls")
        returningPlayer = True
        newPlayer = False
        break
# Checking to see if new player
if (all(playerName != namesList[index][0] for index in range(1, len(namesList)))):
    # The default amounts that a new player starts with
    # Could very easily be adjusted
    playerAccount = 150
    playerMoney = 50
    newPassword = input("Create password: ")
    passwordConfirmation = input("Confirm password: ")
    # Making sure that the password and its confirmation match
    while newPassword != passwordConfirmation:
        os.system('cls')
        print(f"Player: {playerName}\nPasswords do not match.")
        newPassword = input("Create password: ")
        passwordConfirmation = input("Confirm password: ")
    os.system("cls")
    newPlayer = True
    returningPlayer = False

# Main Game Loop
while True:
    # Refilling the card shoe if needed
    # 9 cards would be the amount needed if the player split and the dealer needed 5 (Could be easily adjusted)
    if (len(cardDeck) < 9):
        cardDeck = refillShoe(2)
    # Setting "junk" variables that will be overwritten
    dealerDownCard = -1
    # Setting legitimate variables
    playerWager = 0
    dealerSum = 0
    playerSum = 0
    firstPlayerSum = 0
    secondPlayerSum = 0
    # Resetting the necessary lists
    playerCards = []
    dealerCards = []
    firstPlayerCards = []
    secondPlayerCards = []
    # Showing the player how much money they could bet
    print(f"Money: {playerMoney}")
    # As long as the player has completed at least one hand,
    # going to the bank or exiting the game will work
    print("Bank (b), Quit (q)")
    # Prompting for the wager
    playerWager = input("Wager: ")
    # Clearing screen from previous hand
    updateScreen(masterList)
    # If the player chooses to go the bank
    if (playerWager == "b"):
        # Game will crash if "mainPlayer" is not defined yet (i.e the player has not yet played a hand)
        swissBank(mainPlayer)
        continue
    # If the player chooses to exit the game
    elif (playerWager == "q"):
        writer = csv.writer(namesFile)
        if (newPlayer):
            # Game will crash if "mainPlayer" is not defined yet (i.e the player has not yet played a hand)
            playerInfo = [playerName, passwordConfirmation, mainPlayer.account, mainPlayer.money]
            writer.writerow(playerInfo)
            break
        elif (returningPlayer):
            # Game will crash if "mainPlayer" is not defined yet (i.e the player has not yet played a hand)
            namesList[playerIndex][2] = mainPlayer.account
            namesList[playerIndex][3] = mainPlayer.money
            playerInfo = [playerName, passwordAttempt, mainPlayer.account, mainPlayer.money]
            namesList[playerIndex] = playerInfo
            with open(r"swissBank.csv", 'r+') as namesFile:
                namesFile.truncate(0)
            writer.writerows(namesList)
            break
    # The player is playing the hand
    else:
        playerWager = int(playerWager)
    # Displaying initial four cards
    for elem in range(4):
        # Getting the card that is the dealer's face down card
        if (dealerDownCard == -1):
            dealerDownCard = newCard()
            dealerCards.append(dealerDownCard)
        # Getting the rest of the initial four cards
        chosenCard = newCard()
        # This will be the dealer's hole card
        hiddenCard = createCard("?", "?", 0)
        # The first card (first player card)
        if (elem == 0):
            chosenCard.displayCard(0)
            playerSum += chosenCard.value
            playerCards.append(chosenCard)
        # The second card (dealer hole card)
        elif (elem == 1):
            hiddenCard.displayCard(3)
        # The third card (second player card)
        elif (elem == 2):
            chosenCard.displayCard(1)
            playerSum += chosenCard.value
            playerCards.append(chosenCard)
        # The fourth card (dealer face up card)
        elif (elem == 3):
            chosenCard.displayCard(4)
            dealerSum += chosenCard.value
            dealerCards.append(chosenCard)
        sleep(2)
    # Creating the "main" player
    mainPlayer = createPlayer(playerSum, playerCards, playerWager, playerMoney, playerAccount)
    # Checking the dealer's hidden card for an ace (if dealer face up card.value == 10) (peeking)
    if (dealerCards[1].value == 10 and dealerCards[0].value == 11):
        mainPlayer.money -= mainPlayer.wager
        dealerCards[0].displayCard(3)
        resetMasterList(rowList, masterList)
        print(f"Dealer blackjack")
        playerMoney = mainPlayer.money
        continue
    # Checking player hand for natural blackjack
    if (mainPlayer.sum == 21):
        if (mainPlayer.cards[0].value == 10 and mainPlayer.cards[1].value == 11):
            mainPlayer.money += mainPlayer.possibleGain
            playerMoney = mainPlayer.money
            resetMasterList(rowList, masterList)
            print("Player blackjack")
            continue
        elif (mainPlayer.cards[0].value == 11 and mainPlayer.cards[1].value == 10):
            mainPlayer.money += mainPlayer.possibleGain
            playerMoney = mainPlayer.money
            resetMasterList(rowList, masterList)
            print("Player blackjack")
            continue
    # Allow splitting if the card numbers are the same
    if (mainPlayer.cards[0].number == mainPlayer.cards[1].number):
        # Getting player input for next move
        choice = input("Hit (h), Stand (s), Double Down (d), Split (p): ")
        # Making sure input is valid
        while (choice != "h" and choice != "s" and choice != "d" and choice != "p"):
            updateScreen(masterList)
            choice = input("Invalid choice\nHit (h), Stand (s), Double Down (d), Split (p): ")
    # Restrict splitting if the card numbers are not the same
    else:
        # Getting player input for next move
        choice = input("Hit (h), Stand (s), Double Down (d): ")
        # Making sure input is valid
        while (choice != "h" and choice != "s" and choice != "d"):
            updateScreen(masterList)
            choice = input("Invalid choice\nHit (h), Stand (s), Double Down (d): ")
    # Player chooses to hit
    if (choice == "h"):
        chosenCard = newCard()
        chosenCard.displayCard(2)
        mainPlayer.sum += chosenCard.value
        mainPlayer.cards.append(chosenCard)
        sleep(2)
    # Player chooses to split
    elif (choice == "p"):
        # Wager for each hand is equivalent to the initial wager
        firstWager = playerWager
        secondWager = playerWager
        # Sum for each hand is half of the original sum
        firstPlayerSum = mainPlayer.cards[0].value #playerSum / 2
        secondPlayerSum = mainPlayer.cards[1].value #playerSum / 2
        # Creating player card lists appropriately
        firstPlayerCards.append(mainPlayer.cards[0])
        secondPlayerCards.append(mainPlayer.cards[1])
        # Player choice for first hand
        firstHandChoice = input("Hit (h), Stand (s), Double Down (d): ")
        # First Hand: Player Hits
        if (firstHandChoice == "h"):
            chosenCard = newCard()
            chosenCard.displayCard(8)
            firstPlayerSum += chosenCard.value
            firstPlayerCards.append(chosenCard)
            firstPlayer = createPlayer(firstPlayerSum, firstPlayerCards, firstWager, 0, 0)
        # First Hand: Player Doubles Down
        elif (firstHandChoice == "d"):
            addedWager = int(input(f"Add to Wager (Max: {playerWager}): "))
            chosenCard = newCard()
            chosenCard.displayCard(8)
            firstWager += addedWager
            firstPlayerSum += chosenCard.value
            firstPlayerCards.append(chosenCard)
            firstPlayer = createPlayer(firstPlayerSum, firstPlayerCards, firstWager, 0, 0)
        # First Hand: Player Stands
        elif (firstHandChoice == "s"):
            None
        # Player choice for second hand
        secondHandChoice = input("Hit (h), Stand (s), Double Down (d): ")
        # Second Hand: Player Hits
        if (secondHandChoice == "h"):
            chosenCard = newCard()
            chosenCard.displayCard(9)
            secondPlayerSum += chosenCard.value
            secondPlayerCards.append(chosenCard)
            secondPlayer = createPlayer(secondPlayerSum, secondPlayerCards, secondWager, 0, 0)
        # Second Hand: Player Doubles Down
        elif (secondHandChoice == "d"):
            addedWager = int(input(f"Add to Wager (Max: {playerWager}): "))
            chosenCard = newCard()
            chosenCard.displayCard(9)
            secondWager += addedWager
            secondPlayerSum += chosenCard.value
            secondPlayerCards.append(chosenCard)
            secondPlayer = createPlayer(secondPlayerSum, secondPlayerCards, secondWager, 0, 0)
        # Second Hand: Player Stands
        elif (secondHandChoice == "s"):
            None
    # Player chooses to double down
    elif (choice == "d"):
        addedWager = int(input(f"Add to Wager (Max: {mainPlayer.wager}): "))
        mainPlayer.wager += addedWager
        chosenCard = newCard()
        chosenCard.displayCard(2)
        mainPlayer.sum += chosenCard.value
        mainPlayer.cards.append(chosenCard)
        sleep(2)
    # Player chooses to stand
    elif (choice == "s"):
        None
    # Displaying the dealer's hidden card
    dealerDownCard.displayCard(3)
    dealerSum += dealerDownCard.value
    sleep(2)
    # Position determine where the next displayed card will be displayed
    position = 5
    # The player split
    if (firstPlayerSum != 0):
        players = [firstPlayer, secondPlayer]
    # The player did not split
    else:
        players = [mainPlayer]
    # Doing the final showdown with each of the appropriate players
    for player in players:
        position, playerMoney, dealerSum = finalShowdown(position, player, dealerSum)
# Clear the screen at the termination of the game
os.system('cls')