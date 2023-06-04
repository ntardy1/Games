
#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

bool any(int target, std::vector<int> vector){
    for (int i = 0; i < vector.size(); i++){
        if (vector[i] == target){
            return true;
        }
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
    std::system("cls");
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
    /*
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
    */
    first = "200410007";
    second = "080700002";
    third = "000900050";
    fourth = "007200609";
    fifth = "010006500";
    sixth = "000000080";
    seventh = "005602490";
    eighth = "006800025";
    ninth = "700540060";
    for (int i = 0; i < first.length(); i++){
        std::cout << "Here \n";
        masterVector[0].push_back(static_cast<int>(first[i] - 48));
        std::cout << "First \n";
        masterVector[1].push_back(static_cast<int>(second[i] - 48));
        masterVector[2].push_back(static_cast<int>(third[i] - 48));
        masterVector[3].push_back(static_cast<int>(fourth[i] - 48));
        masterVector[4].push_back(static_cast<int>(fifth[i] - 48));
        masterVector[5].push_back(static_cast<int>(sixth[i] - 48));
        masterVector[6].push_back(static_cast<int>(seventh[i] - 48));
        masterVector[7].push_back(static_cast<int>(eighth[i] - 48));
        masterVector[8].push_back(static_cast<int>(ninth[i] - 48));
        printResults(masterVector);
    }
    int currentNumber;

    // Checking to make sure that the entries are valid
    for (int i = 0; i < masterVector.size(); i++){
        for (int j = 0; j < masterVector[0].size(); j++){
            currentNumber = masterVector[i][j];
            for (int k = 0; k < masterVector[0].size(); k++){
                if (currentNumber == 0){
                    NULL;
                }
                else if (currentNumber == masterVector[i][k] && j != k){
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
    std::vector<int> temp1;
    std::vector<int> temp2;
    std::vector<int> candidates;
    row = 0;
    column = 0;
    counter = 0;
    index = 0;

    while (counter < 9){
        std::cout << "(" << row << ", " << column << ") \n";
        candidates = {1,2,3,4,5,6,7,8,9};
        if (row == 9){
            break;
        }
        if (!any(0, masterVector[row])){
            if (row == 8){
                counter++;
            } else {
                counter++;
                row++;
            }
        } else {
            currentSpot = masterVector[row][column];
            // If at the right edge of the board and the spot is filled, reset column and increase row
            if (currentSpot != 0 && column == 8){
                column = 0;
                row++;
            // If at a filled spot that is not the right edge, increase column
            } else if (currentSpot != 0 && column != 8){
                column++;
            } else {
                // Removing candidates based on the column
                for (int i = 0; i < masterVector.size(); i++){
                    if (masterVector[i][column] != 0 && any(masterVector[i][column], candidates)){
                        candidates.erase(candidates.begin() + getIndex(masterVector[i][column], candidates));
                    }
                }
                // Removing candidates based on the row
                for (int i = 0; i < masterVector.size(); i++){
                    if (masterVector[row][i] != 0 && any(masterVector[row][i], candidates)){
                        candidates.erase(candidates.begin() + getIndex(masterVector[row][i], candidates));
                    }
                }
                // Removing candidates based on local groups
                if (column == 0 || column == 3 || column == 6){
                    if (row == 0 || row == 3 || row == 6){
                        for (int i = 0; i < 3; i++){
                            for (int j = 0; j < 3; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else if (row == 1 || row == 4 || row == 7){
                        for (int i = -1; i < 2; i++){
                            for (int j = 0; j < 3; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else {
                        for (int i = -2; i < 1; i++){
                            for (int j = 0; j < 3; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    }
                } else if (column == 1 || column == 4 || column == 7){
                    if (row == 0 || row == 3 || row == 6){
                        for (int i = 0; i < 3; i++){
                            for (int j = -1; j < 2; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else if (row == 1 || row == 4 || row == 7){
                        for (int i = -1; i < 2; i++){
                            for (int j = -1; j < 2; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else {
                        for (int i = -2; i < 1; i++){
                            for (int j = -1; j < 2; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    }
                } else {
                    if (row == 0 || row == 3 || row == 6){
                        for (int i = 0; i < 3; i++){
                            for (int j = -2; j < 1; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else if (row == 1 || row == 4 || row == 7){
                        for (int i = -1; i < 2; i++){
                            for (int j = -1; j < 2; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    } else {
                        for (int i = -2; i < 1; i++){
                            for (int j = -2; j < 1; j++){
                                if (masterVector[row + i][column + j] != 0 && any(masterVector[row + i][column + j], candidates)){
                                    candidates.erase(candidates.begin() + getIndex(masterVector[row + i][column + j], candidates));
                                }
                            }
                        }
                    }
                }
                for (int i = 0; i < candidates.size(); i++){
                    if (i == 0 && candidates.size() == 1){
                        std::cout << "Candidates: {" << candidates[i] << "} \n";
                    } else if (i == 0){
                        std::cout << "Candidates: {" << candidates[i] << ", ";
                    } else if (i == candidates.size() - 1){
                        std::cout << candidates[i] << "} \n";
                    } else {
                        std::cout << candidates[i] << ", ";
                    }
                }
                // If there is only one candidate left, it has to go in the current spot
                if (candidates.size() == 1){
                    std::cout << "Board changed \n";
                    masterVector[row][column] = candidates[0];
                    row = 0;
                    column = 0;
                    counter = 0;
                } else if (column == 8){
                    column = 0;
                    row++;
                } else {
                    column++;
                }
            }
        }
    }
    if (row == 9){
        std::cout << "Board incompletely solved: \n";
        std::cout << "\n";
        printResults(masterVector);
    } else {
        std::cout << "Puzzle solved: \n";
        printResults(masterVector);
    }
}
