
#include <iostream>
#include <vector>
#include <string>

bool any(int target, std::vector<int> vector){
    for (int i = 0; i < vector.size(); i++){
        if (i == target){
            return true;
        }
    }
    return false;
}

// Determining if target isn't in the vector
bool allNot(int target, std::vector<int> vector){
    int count;
    count = 0;
    for (int i = 0; i < vector.size(); i++){
        if (i != target){
            count++;
        }
    }
    if (count == vector.size()){
        return true;
    }
    return false;
}

void printResults(std::vector<std::vector<int>> masterVector){
    for (int i = 0; i < masterVector.size(); i++){
        for (int j = 0; j < masterVector[i].size(); j++){
            if (j == masterVector[i].size() - 1){
                std::cout << masterVector[i][j] << "\n";
            } else {
                std::cout << masterVector[i][j] << " ";
            }
        }
    }
}

int getIndex(int target, std::vector<int> vector){
    for (int i = 0; i < vector.size(); i++){
        if (vector[i] == target){
            return i;
        }
    }
    return -1;
}

int main(){
    /*
    std::string first;
    std::string second;
    std::string third;
    std::string fourth;
    std::string fifth;
    std::string sixth;
    std::string seventh;
    std::string eighth;
    std::string ninth;
    std::vector<int> firstRow;
    std::vector<int> secondRow;
    std::vector<int> thirdRow;
    std::vector<int> fourthRow;
    std::vector<int> fifthRow;
    std::vector<int> sixthRow;
    std::vector<int> seventhRow;
    std::vector<int> eighthRow;
    std::vector<int> ninthRow;
    std::vector<std::vector<int>> masterVector;
    std::cout << "Enter a zero in any empty spots" << "\n";
    std::cout << "1st Row: ";
    std::cin >> first;
    std::cout << "2nd Row: ";
    std::cin >> second;
    std::cout << "3rd Row: ";
    std::cin >> third;
    std::cout << "4th Row: ";
    std::cin >> fourth;
    std::cout << "5th Row: ";
    std::cin >> fifth;
    std::cout << "6th Row: ";
    std::cin >> sixth;
    std::cout << "7th Row: ";
    std::cin >> seventh;
    std::cout << "8th Row: ";
    std::cin >> eighth;
    std::cout << "9th Row: ";
    std::cin >> ninth;

    for (int i = 0; i < first.length(); i++){
        masterVector[0].push_back(first[i]);
        masterVector[1].push_back(second[i]);
        masterVector[2].push_back(third[i]);
        masterVector[3].push_back(fourth[i]);
        masterVector[4].push_back(fifth[i]);
        masterVector[5].push_back(sixth[i]);
        masterVector[6].push_back(seventh[i]);
        masterVector[7].push_back(eighth[i]);
        masterVector[8].push_back(ninth[i]);
    }
    */
    std::vector<std::vector<int>> masterVector;
    masterVector = {{6,2,4,8,3,0,1,0,7},
                    {0,1,8,9,2,0,3,6,5},
                    {0,0,0,7,6,0,0,4,0},
                    {0,0,0,0,8,0,9,0,1},
                    {0,0,9,0,0,6,0,0,0},
                    {1,4,0,0,0,0,5,8,0},
                    {9,6,0,0,0,8,0,0,3},
                    {0,0,0,0,1,0,0,5,0},
                    {0,7,1,0,4,3,0,0,0}};

    int currentNumber;

    // Checking to make sure that the entries are valid
    for (int i = 0; i < masterVector.size(); i++){
        for (int j = 0; j < masterVector[0].size(); j++){
            currentNumber = masterVector[i][j];
            for (int k = 0; k < masterVector[0].size(); k++){
                if (currentNumber == 0){
                    NULL;
                }
                else if (currentNumber == masterVector[i][k] and j != k){
                    std::cout << "Error in Row " << i + 1 << "\n";
                    break;
                }
            }
        }
    }

    int index;
    int counter;
    int row;
    int column;
    int currentSpot;
    int rowChecker;
    std::vector<int> temp1;
    std::vector<int> temp2;
    std::vector<int> candidates;
    candidates = {0,1,2,3,4,5,6,7,8,9};
    row = 0;
    column = 0;
    counter = 0;
    index = 0;
    rowChecker = 0;

    while (counter < 9){
        candidates = {0,1,2,3,4,5,6,7,8,9};
        if allNot(0, masterVector[row]){
          counter++;
        }
        // For loop (and conditional) to check if the row has been completely solved
        for (int i = 0; i < masterVector.size(); i++){
            if (masterVector[row][i] != 0){
                rowChecker++;
            }
        }
        if (rowChecker == 9 & row == 8){
            counter++;
        } else if (rowChecker == 9){
            row++;
        } else {
            currentSpot = masterVector[row][column];
            // If at the right edge of the board and the spot is filled, reset column and increase row
            if (currentSpot != 0 and column == 8){
                column = 0;
                row++;
            // If at a filled spot that is not the right edge, increase column
            } else if (currentSpot != 0 and column != 8){
                column++;
            } else {
                // Removing candidates based on the column
                for (int i = 0; i < masterVector.size(); i++){
                    if (masterVector[i][column] != 0){
                        candidates.erase(candidates.begin() + getIndex(currentSpot, candidates));
                    }
                }
                // Removing candidates based on the row
                for (int i = 0; i < masterVector.size(); i++){
                    if (masterVector[row][i] != 0){
                        candidates.erase(candidates.begin() + getIndex(currentSpot, candidates));
                    }
                }
                /*
                // Removing candidates based on local groups
                if (column == 0 or column == 3 or column == 6){
                    if (row == 0 or row == 3 or row == 6){
                        for (int i = 0; i < 3; i++){
                            for (int j = 0; j < 3; j++){
                                if (masterVector[row + i][column + j] != 0){
                                candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else if (row == 1 or row == 4 or row == 7){
                        for (int i = -1; i < 2; i++){
                            for (int j = 0; j < 3; j++){
                                if (masterVector[row + i][column + j] != 0){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else {
                        for (int i = -2; i < 1; i++){
                            for (int j = 0; j < 3; j++){
                                if (masterVector[row + i][column + j] != 0){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    }
                } else if (column == 1 or column == 4 or column == 7){
                    if (row == 0 or row == 3 or row == 6){
                        for (int i = 0; i < 3; i++){
                            for (int j = -1; j < 2; j++){
                                if (masterVector[row + i][column + j] != 0){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else if (row == 1 or row == 4 or row == 7){
                        for (int i = -1; i < 2; i++){
                            for (int j = -1; j < 2; j++){
                                if (masterVector[row + i][column + j] != 0){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else {
                        for (int i = -2; i < 1; i++){
                            for (int j = -1; j < 2; j++){
                                if (masterVector[row + i][column + j] != 0){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    }
                } else {
                    if (row == 0 or row == 3 or row == 6){
                        for (int i = 0; i < 3; i++){
                            for (int j = -2; j < 1; j++){
                                if (masterVector[row + i][column + j] != 0){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else if (row == 1 or row == 4 or row == 7){
                        for (int i = -1; i < 2; i++){
                            for (int j = -1; j < 2; j++){
                                if (masterVector[row + i][column + j] != 0){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else {
                        for (int i = -2; i < 1; i++){
                            for (int j = -2; j < 1; j++){
                                if (masterVector[row + i][column + j] != 0){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    }
                }
                */
                // If there is only one candidate left, it has to go in the current spot
                if (candidates.size() == 1){
                    masterVector[row][column] = candidates[0];
                }
                if (column == 8){
                    column = 0;
                    row++;
                } else {
                    column++;
                }
            }
        }
    }
    printResults(masterVector);
}
