// Efficacy dependent on quality of "turnTableWords.txt"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// Checks if a target character is in a string
bool stringTarget(string string, char target){
    for (int i = 0; i < string.size(); i++){
        if (string[i] == target){
            return true;
        }
    }
    return false;
}

// Checks if all the elements of one vector 
// of characters (vector1) can be found in a string
bool vectorString(vector<char> vector, string string){
    int counter;
    counter = 0;
    for (int i = 0; i < vector.size(); i++){
        if (stringTarget(string, vector[i])){
            counter++;
        }
    }
    if (counter == string.size()){
        return true;
    }
    return false;
}

int main(int argc, char *argv[]) {
    string letterString;
    char specialLetter;
    ifstream file;
    vector<char> letters;
    letterString = argv[1];
    for (int i = 0; i <= letterString.size(); i++){
        letters.push_back(letterString[i]);
    }
    specialLetter = letters[0];
    file.open("turnTableWords.txt");
    string currentWord;
    if (file.is_open()){
        while(file){
            getline(file, currentWord);
            if (stringTarget(currentWord, specialLetter)){
                if (vectorString(letters, currentWord)){
                    cout << currentWord << "\n";
                }
            }
        }
    }
    file.close();
}