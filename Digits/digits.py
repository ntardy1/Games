'''
Order of Operations
1) Make the numerical algorithm
2) Deal with output
'''

# Libraries
import os
import random

# Variables
numbers = list(range(6))
operations = []
result = 0 # the current result of all operations

# Functions
def checkDivision(result, tempNumbers):
    removal = False
    # Checking division possibility
    while any(result % num == 0 and num != 1 for num in tempNumbers):
        for num in tempNumbers:
            if (result == num):
                result, tempNumbers = checkSubtraction(result, tempNumbers)
                return result, tempNumbers, removal
            if (result % num == 0 and num != 1):
                result = result / num
                tempNumbers.remove(num)
                removal = True
                break
    return result, tempNumbers, removal

def checkSubtraction(result, tempNumbers):
    removal = False
    # Checking subtraction possibility
    for num1 in tempNumbers:
        while any(((result - num1 == num2 or result - num1 == 0) and num1 != num2) for num2 in tempNumbers):
            for num in tempNumbers:
                if (result - num1 == num or result - num1 == 0):
                    result = result - num1
                    tempNumbers.remove(num1)
                    removal = True
                if (result == 0):
                    return result, tempNumbers, removal
                else:
                    continue
    return result, tempNumbers, removal

def checkResult(result):
    if (result == 0):
        return True
    
def resetTempNumbers(tempNumbers, index_num2, num2, removal):
    # Resetting the tempNumbers list
    if (index_num2 == len(tempNumbers)):
        tempNumbers.append(num2)
    elif (removal == True):
        tempNumbers.insert(index_num2, num2)
    else:
        tempNumbers[index_num2] = num2

# Algorithm
os.system('cls')
targetNumber = int(input('Please enter the target number: ')) # Getting the target numbers
result = targetNumber

# Getting the given numbers (which will be used to obtain the target number)
numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5] = input('Please enter the given numbers: ').split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

counter = 0
randomNumber = 0 #random.randint(0, 1)
while (result != 0):
    counter += 1
    if (randomNumber == 0 and counter != 1):
        randomNumber = 1
    elif (randomNumber == 1 and counter != 1):
        randomNumber = 0
    tempNumbers = numbers # Temporary numbers list which will be modified as the result changes
    result = targetNumber
    print(f'Iteration: {counter} \ntempNumbers = {tempNumbers}')

    # Checking multiplication first
    if (randomNumber == 0):
        # Checking possibility of multiple elements' multiplication
        for num1 in tempNumbers:
            if (num1 == 1):
                continue
            else:
                index_num1 = tempNumbers.index(num1)
                tempNumbers.remove(num1)
                for num2 in tempNumbers:
                    index_num2 = tempNumbers.index(num2)
                    tempMultiplication = num1 * num2
                    tempNumbers[index_num2] = tempMultiplication
                    # Checking division possibility
                    result, tempNumbers, removal = checkDivision(result, tempNumbers)
                    if (result == 0):
                        break
                    resetTempNumbers(tempNumbers, index_num2, num2, removal)
                    # Checking subtraction possibility
                    result, tempNumbers, removal = checkSubtraction(result, tempNumbers)
                    if (result == 0):
                        break
                    resetTempNumbers(tempNumbers, index_num2, num2, removal)
                if (result == 0):
                    break
                tempNumbers.insert(index_num1, num1)
        if (result == 0):
            break
        # Checking the possibility of multiple elements' addition
        for num1 in tempNumbers:
            index_num1 = tempNumbers.index(num1)
            tempNumbers.remove(num1)
            for num2 in tempNumbers:
                index_num2 = tempNumbers.index(num2)
                tempAddition = num1 + num2
                tempNumbers[index_num2] = tempAddition
                # Checking division possibility
                result, tempNumbers, removal = checkDivision(result, tempNumbers)
                if (result == 0):
                        break
                resetTempNumbers(tempNumbers, index_num2, num2, removal)
                # Checking subtraction possibility
                result, tempNumbers, removal = checkSubtraction(result, tempNumbers)
                if (result == 0):
                        break
                resetTempNumbers(tempNumbers, index_num2, num2, removal)
            if (result == 0):
                break
            tempNumbers.insert(index_num1, num1)
        if (result == 0):
            break
        print(f'Result: {result}')

    # Checking addition first
    elif (randomNumber == 1):
        # Checking the possibility of multiple elements' addition
        for num1 in tempNumbers:
            index_num1 = tempNumbers.index(num1)
            tempNumbers.remove(num1)
            for num2 in tempNumbers:
                index_num2 = tempNumbers.index(num2)
                tempAddition = num1 + num2
                tempNumbers[index_num2] = tempAddition
                # Checking division possibility
                result, tempNumbers, removal = checkDivision(result, tempNumbers)
                if (result == 0):
                        break
                resetTempNumbers(tempNumbers, index_num2, num2, removal)
                # Checking subtraction possibility
                result, tempNumbers, removal = checkSubtraction(result, tempNumbers)
                if (result == 0):
                        break
                resetTempNumbers(tempNumbers, index_num2, num2, removal)
            if (result == 0):
                break
            tempNumbers.insert(index_num1, num1)
        if (result == 0):
            break
        # Checking possibility of multiple elements' multiplication
        for num1 in tempNumbers:
            if (num1 == 1):
                continue
            else:
                index_num1 = tempNumbers.index(num1)
                tempNumbers.remove(num1)
                for num2 in tempNumbers:
                    index_num2 = tempNumbers.index(num2)
                    tempMultiplication = num1 * num2
                    tempNumbers[index_num2] = tempMultiplication
                    # Checking division possibility
                    result, tempNumbers, removal = checkDivision(result, tempNumbers)
                    if (result == 0):
                        break
                    resetTempNumbers(tempNumbers, index_num2, num2, removal)
                    # Checking subtraction possibility
                    result, tempNumbers, removal = checkSubtraction(result, tempNumbers)
                    if (result == 0):
                        break
                    resetTempNumbers(tempNumbers, index_num2, num2, removal)
                if (result == 0):
                    break
                tempNumbers.insert(index_num1, num1)
        if (result == 0):
            break
        print(f'Result: {result}')
    if (counter == 2):
        break

if (counter == 2):
    print('Failure')
else:
    print('Success')
