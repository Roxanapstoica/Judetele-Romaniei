from turtle import Turtle, Screen
import pandas as pd

BACKGROUND = "romania_map_blank.gif"

screen = Screen()
state_to_be_written = Turtle()
background_map = Turtle()

state_to_be_written.penup()
state_to_be_written.hideturtle()

screen.title("Judetele Romaniei")
screen.addshape(BACKGROUND)
background_map.shape(BACKGROUND)

legend = Turtle()
legend.color("green")
legend.hideturtle()
legend.penup()
legend.goto(-250,210)
legend.write("Pentru a iesi tasteaza Exit\nScrie numele judetelor fara diacritice\nFoloseste spatiul in loc de cratima")
answer_state = screen.textinput(title="Ghiceste judetele", prompt="Care e judetul? Tasteaza Exit pentru iesire")
data = pd.read_csv("42-judete.csv")
counter = 0
guess = 0
guessed_judete = []
while counter < 42:
    answer_state = answer_state.title()
    map_state = data[data.state == answer_state]
    if answer_state == "Exit":
        states_to_learn = list(set(data.state.to_list()) - set(guessed_judete))
        states_to_learn = pd.DataFrame(states_to_learn)
        states_to_learn.to_csv("./states_to_learn.csv")
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(-50,-230)
        t.color("red")
        t.write("Vezi judetele pe care nu le-ai ghicit in fisierul states_to_learn.csv")
        break
    if len(map_state) > 0:
        guess += 1
        counter += 1
        state_to_be_written.goto(int(map_state.x), int(map_state.y))
        state_to_be_written.write(answer_state)
        guessed_judete.append(answer_state)
    answer_state = screen.textinput(title=f"{guess}/42 corecte", prompt="Urmatorul judet? Tasteaza Exit pentru iesire")


screen.exitonclick()