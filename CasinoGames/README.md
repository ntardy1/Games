# terminalSize.py
This is a script that will use user input to determine the width and length of the current open command prompt window, measured in keyboard characters. When the dash is moving horizontally, the 'esc' key should be pressed once one dash reaches the second row of the command prompt window. When the dash is moving vertically, the 'esc' key should be pressed once the dash reaches one row below the main viewing area. It was not until after I wrote this program that I discovered the os.get_terminal_size() function. Therefore, the [blackjack.py](blackjack.py) script does not use this function for determining the current window size. 

# blackjack.py
This is a script that plays the game of blackjack by utilizing user input for player decision and the command window/keyboard symbols as the GUI. It gets the terminal dimensions using the os.get_terminal_size() function (with a little bit taken off of the length to allow room for game output and player input at the end of each hand). For Blackjack rules and instructions, visit [here](https://en.wikipedia.org/wiki/Blackjack).

A few notes about the game format, usage, etc...

1) "Player Account" refers to how much money the player has in their bank account (in game). This money must first be withdrawn in order to be available for wagering.

2) "Player Money" refers to how much money the player has currently withdrawn from their account. This money is available for wagering.

3) If the dealer has five cards on the "table" and has not yet reached 17/in between 17 and 21 and is still losing to the player, the game will display the next dealer card over the rightmost one. In the program's current state, this will completely hide the card that was previously there, but the dealer's sum will be correctly updated.

4) When the game is intialized, the player must complete one hand before visiting the bank or quitting the game. Failure to do this will result in the game crashing (as a result of the sequential way it is written).
