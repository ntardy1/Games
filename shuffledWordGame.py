
# Libraries
import random

rawData = open("WordsFile.txt", "r")
dataset = rawData.readlines()
rawData.close()

allWordsList = []
for elem in dataset:
    elemLength = len(elem)
    allWordsList.append(elem[0:len(elem) - 1])

randomNumber = random.randint(0, len(allWordsList) - 1)
chosenWord = allWordsList[randomNumber]
shuffledWord = ''.join(random.sample(chosenWord, len(chosenWord)))

# Delete this line before production!!!!!!
# print(f"{chosenWord},{shuffledWord}")

hintsList = []
print(shuffledWord)
guess = str(input("Guess the word: "))
guessNumber = 1
while guess != chosenWord and guessNumber <= 5:
    hintsList = []
    print("That is incorrect. Try again.")
    for elem in chosenWord:
        if elem == guess[chosenWord.index(elem)]:
            hintsList.append(1)
        else:
            hintsList.append(0)
    hintsList = [str(i) for i in hintsList]
    hints = ''.join(hintsList)
    print(f"Hints: {hints}")
    guess = str(input("Guess the word: "))

print('That is the correct word!')
