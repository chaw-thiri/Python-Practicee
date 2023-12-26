# Guess the 50 States Game🗺️
This Python script utilizes the Turtle graphics library and pandas to create an interactive game called "Guess the 50 States." The game displays a map of the United States, and the user is prompted to guess the names of each state. The user can exit the game at any time, and the script will save the remaining states to a CSV file for further learning.

## Usage
Ensure you have the required dependencies installed, particularly turtle and pandas.


## Gameplay
The game displays a map of the United States with state borders and names hidden.    
The user is prompted to guess the names of the states by entering them through the input dialog.   
Typing "Exit" at any time allows the user to exit the game.   
After exiting, the script saves the remaining states to a CSV file named "States_to_learn.csv."   
### Notes
The game uses the Turtle graphics library to display the map and mark correctly guessed states.   
**Pandas** is used to read state data from the "50_states.csv" file.      

The game keeps track of the number of correct guesses, and the user can exit the game at any time.   
The remaining states (those not guessed) are saved to **"States_to_learn.csv"** for further study.   
