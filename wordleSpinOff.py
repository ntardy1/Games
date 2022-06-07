
# A program to make a spin off of the popular (as of 1.12.22) word game "Wordle"

# Modules
import random
rawData = open("WordsFile.txt", "r")
dataset = rawData.readlines()
rawData.close()

allWordsList = []
for elem in dataset:
    allWordsList.append(elem[0:len(elem) - 1])

randomNumber = random.randint(0, len(allWordsList) - 1)
chosenWord = allWordsList[randomNumber]

hintsList = []
guessNumber = 1
guess = str(input("Guess the word: "))
while guess != chosenWord and guessNumber <= 6:
    if guessNumber == 6:
        print(f"The word was '{chosenWord}'.")
        break
    elif guess == chosenWord:
        print(f"That is correct!")
    else:
        hintsList = []
        for elem in guess:
            if elem == chosenWord[guess.index(elem)]:
                hintsList.append('2')
            elif any(elem == i for i in chosenWord):
                hintsList.append('1')
            else:
                hintsList.append('0')
        hints = ''.join(hintsList)
        print(f"Hints: {hints} \nGuesses Left: {6 - guessNumber}")
        guessNumber += 1
        guess = str(input("Guess the word: "))
