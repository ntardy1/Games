'''
Order of Operations
1) Make the numerical algorithm
2) Deal with output
'''

# Libraries
import os

# Variables
numbers = list(range(6))
numbersUsed = []
operationsUsed = []
operations = list(range(4))
operations_possibilities = ["+", "-", "*", "/"]
firstTensor = []
tempFirstTensor = []
result = False
newGivens = []

firstNumberUsed_1 = -1
firstNumberUsed_2 = -1

# Functions

# Function to print the sdolution steps
def printResults(*args):
    for index in range(0, len(numbersUsed), 2):
        print(f"{numbersUsed[index]} {operations_possibilities[operationsUsed[(int(index/2))]]} {numbersUsed[index+1]} = {newGivens[int(index/2)]}")
    if (len(args) > 0):
        if (args[0] == 0): # came from the "check" function
            print(f"{args[1]} {operations_possibilities[operations_possibilities.index(args[2])]} {args[3]} = {target}") # args[2] specifies the operation
        elif (args[0] == 1): # came from the "intermediateCheck" function
            if (args[1] == 0): # parentheses around the first operation
                print(f"({args[2]} {operations_possibilities[operations_possibilities.index(args[3])]} {args[4]}) {operations_possibilities[operations_possibilities.index(args[5])]} {args[6]} = {target}")
            elif (args[1] == 1): # parentheses around the second operation
                print(f"{args[2]} {operations_possibilities[operations_possibilities.index(args[3])]} ({args[4]} {operations_possibilities[operations_possibilities.index(args[5])]} {args[6]}) = {target}")
    
# Function to see if any of the remaining givens can be combined with a current number to make the target
# or if the current number is equal to the target
def check(remainingGivens, currentNumber, target):
    if (currentNumber == target):
        newGivens.append(currentNumber)
        printResults()
        return True
    for given in remainingGivens:
        if (given + currentNumber == target):
            numbersUsed.append(given)
            numbersUsed.append(currentNumber)
            operationsUsed.append(0)
            printResults()
            return True
        elif (given - currentNumber == target):
            numbersUsed.append(given)
            numbersUsed.append(currentNumber)
            operationsUsed.append(1)
            printResults()
            return True
        elif (given * currentNumber == target):
            numbersUsed.append(given)
            numbersUsed.append(currentNumber)
            operationsUsed.append(2)
            printResults()
            return True
        elif (currentNumber != 0 and given / currentNumber == target):
            numbersUsed.append(given)
            numbersUsed.append(currentNumber)
            operationsUsed.append(3)
            printResults()
            return True
    return False

# Function to check if any of the given numbers in newGivens can combine to make the target
def intermediateCheck(newGivens, target):
    for given in newGivens:
        temp_1 = list(newGivens)
        temp_2 = list(temp_1)
        temp_1.remove(given)
        temp_2.remove(given)
        for given_1 in temp_1:
            temp_2.remove(given_1)
            for given_2 in temp_2:
                # Parentheses around the first operation
                # Addition first step
                if ((given + given_1) + given_2 == target):
                    printResults(1, 0, given, "+", given_1, "+", given_2)
                    return True
                elif ((given + given_1) - given_2 == target):
                    printResults(1, 0, given, "+", given_1, "-", given_2)
                    return True
                elif ((given + given_1) * given_2 == target):
                    printResults(1, 0, given, "+", given_1, "*", given_2)
                    return True
                elif (given_2 != 0 and (given + given_1) / given_2 == target):
                    printResults(1, 0, given, "+", given_1, "/", given_2)
                    return True
                # Subtraction first step
                elif ((given - given_1) + given_2 == target):
                    printResults(1, 0, given, "-", given_1, "+", given_2)
                    return True
                elif ((given - given_1) - given_2 == target):
                    printResults(1, 0, given, "-", given_1, "-", given_2)
                    return True
                elif ((given - given_1) * given_2 == target):
                    printResults(1, 0, given, "-", given_1, "*", given_2)
                    return True
                elif (given_2 != 0 and (given - given_1) / given_2 == target):
                    printResults(1, 0, given, "-", given_1, "/", given_2)
                    return True
                # Multiplication first step
                elif ((given * given_1) + given_2 == target):
                    printResults(1, 0, given, "*", given_1, "+", given_2)
                    return True
                elif ((given * given_1) - given_2 == target):
                    printResults(1, 0, given, "*", given_1, "-", given_2)
                    return True
                elif ((given * given_1) * given_2 == target):
                    printResults(1, 0, given, "*", given_1, "*", given_2)
                    return True
                elif (given_2 != 0 and (given * given_1) / given_2 == target):
                    printResults(1, 0, given, "*", given_1, "/", given_2)
                    return True
                # Division first step
                elif (given_1 != 0 and (given / given_1) + given_2 == target):
                    printResults(1, 0, given, "/", given_1, "+", given_2)
                    return True
                elif (given_1 != 0 and (given / given_1) - given_2 == target):
                    printResults(1, 0, given, "/", given_1, "-", given_2)
                    return True
                elif (given_1 != 0 and (given / given_1) * given_2 == target):
                    printResults(1, 0, given, "/", given_1, "*", given_2)
                    return True
                elif (given_1 != 0 and given_2 != 0 and (given / given_1) / given_2 == target):
                    printResults(1, 0, given, "/", given_1, "/", given_2)
                    return True
                # Parentheses around the second operation
                # Addition first step
                if (given + (given_1 + given_2) == target):
                    printResults(1, 1, given, "+", given_1, "+", given_2)
                    return True
                elif (given + (given_1 - given_2) == target):
                    printResults(1, 1, given, "+", given_1, "-", given_2)
                    return True
                elif (given + (given_1 * given_2) == target):
                    printResults(1, 1, given, "+", given_1, "*", given_2)
                    return True
                elif (given_2 != 0 and given + (given_1 / given_2) == target):
                    printResults(1, 1, given, "+", given_1, "/", given_2)
                    return True
                # Subtraction first step
                elif (given - (given_1 + given_2) == target):
                    printResults(1, 1, given, "-", given_1, "+", given_2)
                    return True
                elif (given - (given_1 - given_2) == target):
                    printResults(1, 1, given, "-", given_1, "-", given_2)
                    return True
                elif (given - (given_1 * given_2) == target):
                    printResults(1, 1, given, "-", given_1, "*", given_2)
                    return True
                elif (given_2 != 0 and given - (given_1 / given_2) == target):
                    printResults(1, 1, given, "-", given_1, "/", given_2)
                    return True
                # Multiplication first step
                elif (given * (given_1 + given_2) == target):
                    printResults(1, 1, given, "*", given_1, "+", given_2)
                    return True
                elif (given * (given_1 - given_2) == target):
                    printResults(1, 1, given, "*", given_1, "-", given_2)
                    return True
                elif (given * (given_1 * given_2) == target):
                    printResults(1, 1, given, "*", given_1, "*", given_2)
                    return True
                elif (given_2 != 0 and given * (given_1 / given_2) == target):
                    printResults(1, 1, given, "*", given_1, "/", given_2)
                    return True
                # Division first step
                elif (given_1 + given_2 != 0 and given / (given_1 + given_2) == target):
                    printResults(1, 1, given, "/", given_1, "+", given_2)
                    return True
                elif (given_1 - given_2 != 0 and given / (given_1 - given_2) == target):
                    printResults(1, 1, given, "/", given_1, "-", given_2)
                    return True
                elif (given_1 * given_2 != 0 and given / (given_1 * given_2) == target):
                    printResults(1, 1, given, "/", given_1, "*", given_2)
                    return True
                elif (given_1 * given_2 != 0 and given_2 != 0 and given / (given_1 / given_2) == target):
                    printResults(1, 1, given, "/", given_1, "/", given_2)
                    return True
    return False

# Function to create a tensor
def createTensor(givens, operations, tensor):
    tempOperations = list(operations)
    tempOperations.append(tempOperations[len(tempOperations) - 1]+1)
    columns = len(givens) - 1
    for num in givens:
        tensor.append([0]*(len(tempOperations)))
        for operation in tempOperations:
            tensor[givens.index(num)][tempOperations.index(operation)] = [0]*columns
    return tensor

# Function to fill a tensor
def fillTensor(tensor, givens, operations):
    rows = list(operations)
    rows.append(4)
    columns = len(givens)
    for matrix in tensor:
        for row in rows:
            if (row == 0): # Adding a row of the other given numbers for future reference
                matrix[row] = [num for num in givens]
                matrix[row].remove(givens[tensor.index(matrix)])
            if (row == 1): # Addition
                matrix[row] = [givens[tensor.index(matrix)] + givens[column] for column in range(columns)]
                matrix[row].remove(givens[tensor.index(matrix)] + givens[tensor.index(matrix)])
            elif (row == 2): # Subtraction
                matrix[row] = [givens[tensor.index(matrix)] - givens[column] if givens[tensor.index(matrix)] - givens[column] >= 0 else 0 for column in range(columns)]
                matrix[row].remove(0)
            elif (row == 3): # Multiplication
                matrix[row] = [givens[tensor.index(matrix)] * givens[column] for column in range(columns)]
                matrix[row].remove(givens[tensor.index(matrix)] * givens[tensor.index(matrix)])
            elif (row == 4): # Division
                if all(givens[column] != 0 for column in range(columns)):
                    matrix[row] = [givens[tensor.index(matrix)] / givens[column] if (givens[tensor.index(matrix)] % givens[column] == 0) else 0 for column in range(columns)]
                else:
                    matrix[row] = [0]*(columns-1)
                matrix[row].remove(1) if any(num == 1 for num in matrix[row]) else None
    return tensor

# Algorithm
os.system('cls')

target = int(input('Please enter the target number: '))

givens = input('Please enter the given numbers: ').split()
givens = [int(num) for num in givens]

# Creating the first tensor
firstTensor = createTensor(givens, operations, [])

# Filling the first tensor
firstTensor = fillTensor(firstTensor, givens, operations)

tempFirstTensor = list(firstTensor) # Creating a tensor that will be iteratively modified
tempGivens_1 = list(givens) # Creating a list of the givens that will be iteratively modified

# Testing all first-step operations
columns = len(givens)
for matrix_1 in firstTensor: # Iterating through to get the first number (that is the result of a previous operation)
    columns -= 1

# Obtaining (and testing) a first-step operation
for matrix_1 in firstTensor: # Iterating through to get the first number (that is the result of a previous operation)
    columns_1 = len(givens) - 1
    tempGivens_1 = list(givens)
    tempFirstTensor = list(firstTensor)
    tempFirstTensor.remove(matrix_1) # Removing the current matrix
    tempGivens_1.remove(tempGivens_1[firstTensor.index(matrix_1)]) # Removing the first number used from tempGivens_1
    for operation in operations: # Going through each row of the current matrix_1
        operationsUsed = [] # Resetting the operationsUsed list
        operationsUsed.append(operation)
        for column in list(range(columns_1)): # Going through each column of the current matrix_1
            newGivens = [] # Resetting the newGivens list
            numbersUsed = [] # Resetting the numbersUsed list
            firstNumberUsed = givens[firstTensor.index(matrix_1)] # Keeping track of the first number used for the first operation
            numbersUsed.append(firstNumberUsed)
            secondNumberUsed = matrix_1[0][column] # Keeping track of the second number used for the first operation
            numbersUsed.append(secondNumberUsed)
            tempGivens_1.remove(secondNumberUsed)
            firstNumber = matrix_1[operation+1][column] # +1 because the first row is just the givens
            newGivens.append(firstNumber) # Adding the first number (from computations) to the newGivens list
            result = check(tempGivens_1, firstNumber, target) # Essentially checking if the puzzle is two-operation solvable
            if (result):
                break
            for matrix_2 in tempFirstTensor: # Removing the matrix that corresponds to the second number used
                if all(secondNumberUsed != num for num in matrix_2[0]):
                    tempFirstTensor.remove(matrix_2)
                    break
            # Obtaining a second step operation
            for matrix_3 in tempFirstTensor: # Iterating through to get the second number (that is the result of a previous operation)
                columns_2 = len(givens) - 1
                tempGivens_2 = list(tempGivens_1)
                tempSecondTensor = list(tempFirstTensor)
                tempSecondTensor.remove(matrix_3)
                tempGivens_2.remove(tempGivens_2[tempFirstTensor.index(matrix_3)])
                for operation_2 in operations: # Going through each row of the current matrix_3
                    operationsUsed.append(operation_2)
                    for column_2 in list(range(columns_2)): # Going through each column of the current matrix_3
                        numbersUsed = numbersUsed[0:2]
                        firstNumberUsed_1 = tempGivens_1[tempFirstTensor.index(matrix_3)] # Keeping track of the first number used in the second operation
                        numbersUsed.append(firstNumberUsed_1)
                        if any(givens[column_2] == num for num in tempGivens_1) and all(givens[column_2] != num for num in numbersUsed):
                            secondNumberUsed_1 = matrix_3[0][matrix_3[0].index(givens[column_2])] # Keeping track of the second number used in the second operation
                            numbersUsed.append(secondNumberUsed_1)
                        else:
                            continue
                        tempGivens_2.remove(secondNumberUsed_1)
                        secondNumber = matrix_3[operation_2+1][matrix_3[0].index(givens[column_2])] # +1 because the first row is just the givens
                        newGivens.append(secondNumber)
                        result = intermediateCheck(newGivens + tempGivens_2, target)
                        if (result):
                            break
                        for matrix_4 in tempSecondTensor: # Removing the matrix that corresponds to the second number used
                            if all(secondNumberUsed_1 != num for num in matrix_4[0]):
                                tempSecondTensor.remove(matrix_4)
                                break
                        # Obtaining a third step operation
                        for matrix_5 in tempSecondTensor: # Iterating through to get the second number (that is the result of a previous operation)
                            columns_3 = len(givens) - 1
                            tempGivens_3 = list(tempGivens_2)
                            tempThirdTensor = list(tempSecondTensor)
                            tempThirdTensor.remove(matrix_5)
                            tempGivens_3.remove(tempGivens_2[tempSecondTensor.index(matrix_5)])
                            for operation_3 in operations: # Going through each row of the current matrix_5
                                operationsUsed.append(operation_3)
                                for column_3 in list(range(columns_3)): # Going through each column of the current matrix_5
                                    numbersUsed = numbersUsed[0:4]
                                    firstNumberUsed_2 = tempGivens_2[tempSecondTensor.index(matrix_5)]
                                    numbersUsed.append(firstNumberUsed_2)
                                    secondNumberUsed_2 = tempGivens_3[0] # Keeping track of the second number used in the third operation
                                    numbersUsed.append(secondNumberUsed_2)
                                    tempGivens_3.remove(secondNumberUsed_2)
                                    thirdNumber = matrix_5[operation_3+1][matrix_5[0].index(secondNumberUsed_2)]  # +1 because the first row is just the givens
                                    newGivens.append(thirdNumber)
                                    result = intermediateCheck(newGivens + tempGivens_3, target)
                                    if (result):
                                        break
                                    for matrix_6 in tempThirdTensor: # Removing the matrix that corresponds to the second number used
                                        if all(secondNumberUsed_2 != num for num in matrix_6[0]):
                                            tempThirdTensor.remove(matrix_6)
                                            break
                                    # Performing the "second stage" of operations
                                    secondTensor = createTensor(newGivens, operations, [])
                                    secondTensor = fillTensor(secondTensor, newGivens, operations)
                                    for matrix_1_1 in secondTensor: # Iterating through each number in the newGivens list
                                        columns_1_1 = len(newGivens) - 1
                                        tempNewGivens = list(newGivens)
                                        tempFirstTensor_1 = list(secondTensor)
                                        tempFirstTensor_1.remove(matrix_1_1) # Removing the current matrix
                                        tempNewGivens.remove(tempNewGivens[secondTensor.index(matrix_1_1)]) # Removing the first number used from tempNewGivens
                                        for operation_1_1 in operations: # Going through each row of the current matrix_1_1
                                            for column_1_1 in list(range(columns_1_1)): # Going through each column of the current matrix_1_1
                                                numbersUsed = numbersUsed[0:6]
                                                operationsUsed.append(operation_1_1)
                                                firstNumberUsed_1_1 = newGivens[secondTensor.index(matrix_1_1)] # Keeping track of the first number used for the first operation of the second stage
                                                numbersUsed.append(firstNumberUsed_1_1)
                                                secondNumberUsed_1_1 = matrix_1_1[0][column_1_1] # Keepging track of the second number used in the first operation of the second stage
                                                numbersUsed.append(secondNumberUsed_1_1)
                                                tempNewGivens.remove(secondNumberUsed_1_1)
                                                firstNumber_1 = matrix_1_1[operation_1_1+1][column_1_1] # +1 because the first row is just givens
                                                result = check(tempNewGivens, firstNumber_1, target)
                                                if (result):
                                                    break
                                                tempNewGivens.insert(column_1_1, secondNumberUsed_1_1)
                                                operationsUsed.remove(operation_1_1)
                                            if (result):
                                                break
                                        if (result):
                                            break
                                    if (result):
                                        break
                                    newGivens.remove(thirdNumber)
                                    tempGivens_3.insert(tempSecondTensor.index(matrix_5), secondNumberUsed_2)
                                    tempThirdTensor.insert(tempGivens_3.index(secondNumberUsed_2), matrix_6)
                                if (result):
                                    break
                                operationsUsed.remove(operation_3)
                            if (result):
                                break
                        if (result):
                            break
                        newGivens.remove(secondNumber)
                        tempGivens_2.insert(tempFirstTensor.index(matrix_3), secondNumberUsed_1)
                        tempSecondTensor.insert(tempGivens_2.index(secondNumberUsed_1), matrix_4)
                    if (result):
                        break
                    operationsUsed.remove(operation_2)
                if (result):
                    break
            if (result):
                break
            newGivens.remove(firstNumber)
            tempGivens_1.insert(column, secondNumberUsed) # Replacing the second number used
            tempFirstTensor.insert(tempGivens_1.index(secondNumberUsed), matrix_2) # Replacing the matrix corresponding to the second number used
        if (result):
            break
    if (result):
        break

if (result):
    print("Success")
else:
    print("Algorithm cannot solve puzzle")