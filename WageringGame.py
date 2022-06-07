
# A Script for A Probablility-Based Wagering Game
# Importing modules
import random
import os

# Creating a file for storing player highscores
#Highscores = open("Highscores.txt", "x") # Creating the file if it doesn't already exist
Highscores = open("Highscores.txt", "r+") # Once the file exists, open it for editing

# INSTEAD OF CHANGING DICTIONARY VALUES, TURN DICTIONARY INTO A LIST
os.system('cls')
# Getting player's name
playerName = input("Please enter your player name: ")

# Declaring variables
money = 100
highscore = 100
highscoresDict = {playerName: highscore}

while (money > 0):
    randomUpperBound = random.randrange(2, 10, 1)
    chosenNumber = int(input(f"Please choose a number to wager on (Min: 1   Max: {randomUpperBound}): "))
    wagerAmount = int(input(f"Enter amount to wager (Min: 1  Max: {money}): "))
    correctNumber = random.randrange(1, randomUpperBound,1)
    if (chosenNumber == correctNumber):
        money += wagerAmount
        highscore = money
        os.system('cls')
        print(f"You won! You now have {money} dollars!")
    elif (chosenNumber != correctNumber):
        money -= wagerAmount
        os.system('cls')
        print(f"You lost! The number was {correctNumber}.")
        print(f"You now have {money} dollars.")

score = highscoresDict[playerName]
if highscore > score:
    highscore = highscoresDict[playerName]

Highscores.write(f"\n{highscoresDict}")
print(f"Player: {playerName} \nHighscore: {score}")
