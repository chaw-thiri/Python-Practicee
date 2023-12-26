# turtle only works with git file
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Guess the 50 states game")
img = "blank_states_img.gif"
screen.addshape(img)  # only after adding image file in here , turtle can use the image
turtle.shape(img)

dataFile = pd.read_csv("50_states.csv")
stateData = dataFile.state.to_list()

guessedStates = []
result = 0
while len(guessedStates) < len(stateData):

    ansState = screen.textinput(title=f"{result}/50 guesses", prompt="What's is the name of the state?").title()
    if ansState == "Exit":
        remainingStates = []
        for state in stateData:
            if state not in guessedStates:
                remainingStates.append(state)
        dataToLearn = pd.DataFrame(remainingStates)
        dataToLearn.to_csv("States_to_learn.csv")
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


# def getMouseClickCoordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(getMouseClickCoordinate)  # when the mouse is clicked, this function would be called
# turtle.mainloop()  # will keep the screen open

screen.exitonclick()
