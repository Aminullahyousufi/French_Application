import pandas
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.title("Lets Learn French")
image = "screen.gif"
screen.addshape(image)
timmy.shape(image)

data = pandas.read_csv("french_number.csv")
new_data = data.to_dict()
guessed_answer = []

while len(guessed_answer) < 21:
    answer = screen.textinput(title="French Number", prompt="please count French number from 1 to 20:").title()
    incorrect_answer = []

    for ans in new_data:
        if ans not in guessed_answer:
            incorrect_answer.append(ans)
    new_file = pandas.DataFrame(incorrect_answer)
    new_file.to_csv("Words_to_Learn.csv")
    if answer == "Exit":
        break
    if guessed_answer in data:
        guessed_answer.append(answer)
        answer_data = data[new_data == guessed_answer]