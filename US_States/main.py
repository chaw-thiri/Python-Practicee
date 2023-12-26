# turtle only works with git file
import turtle
import pandas as pd
import time
from tkinter import messagebox


def exit(msg="You typed Exit"):
    """ending the game"""
    remainingStates = []
    for state in stateData:
        if state not in guessedStates:
            remainingStates.append(state)
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    messagebox.showinfo(msg,
                        f"Your score: {result}/50"
                        f"\nTime taken:{elapsed_time} seconds.\n")
    dataToLearn = pd.DataFrame(remainingStates)
    dataToLearn.to_csv("States_to_learn.csv")


screen = turtle.Screen()  # bring a canvas on the display using turtle module
screen.title("Guess the 50 states game")  # set gametitle

# SETTING BACKGROUND IMAGE
img = "blank_states_img.gif"
screen.addshape(img)  # only after adding image file in here , turtle can use the image
turtle.shape(img)

# ANSWER DATA
dataFile = pd.read_csv("50_states.csv")
stateData = dataFile.state.to_list()

guessedStates = []
result = 0
error_count = 0

# SHOW HOW MUCH TIME THE USER SPENT
start_time = time.time()
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(0, -280)

# TO SHOW ERROR COUNT : THE GAME WILL STOP IF THE USER WRONGS FOR 3 TIME
error_display = turtle.Turtle()
error_display.hideturtle()
error_display.penup()
error_display.goto(-140, -280)

while len(guessedStates) < len(stateData):

    # FOR SHOWING ERROR COUNT
    error_display.clear()
    error_display.write(f"Error: {error_count}", align="center", font=("Verdana", 14, "normal"))
    # FOR SHOWING TIME SPENT
    elapsed_time = round(time.time() - start_time, 2)
    timer_display.clear()
    timer_display.write(f"Time: {int(elapsed_time)} seconds", align="center", font=("Verdana", 14, "normal"))
    # PROMPT FOR ANSWER
    ansState = screen.textinput(title=f"{result}/50 guesses", prompt="What's is the name of the state?").title()

    # COLLECTING ANSWER
    if ansState == "Exit" or error_count == 3:
        exit()
        break

    if ansState in stateData:
        result += 1
        guessedStates.append(ansState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        location = dataFile[dataFile.state == ansState]
        t.goto(int(location.x.iloc[0]), int(location.y.iloc[0]))
        t.write(ansState)

    else:
        error_count += 1
        error_display.clear()
        error_display.write(f"Error: {error_count}", align="center", font=("Verdana", 14, "normal"))
        if error_count == 3:
            msg = "You did 3 mistakes.Game Over."
            exit(msg)
            break

screen.exitonclick()
