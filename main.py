import turtle
import pandas as pd

file = pd.read_csv("50_states.csv")

df = pd.DataFrame = file
all_states = df.state.to_list()
states_guessed = []
screen = turtle.Screen()
screen.title(f"U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()


def has_state_been_guessed(state):
    if state in states_guessed:
        return True
    else:
        return False


while len(states_guessed) < 50:
    answer_state = screen.textinput(f"Guess the state!   {len(states_guessed)}/50", "Name a state: ").title()
    if answer_state == "Exit":
        missing_states = [n for n in all_states if n not in states_guessed]
        break
    if not df[df.state == answer_state].state.empty:
        if has_state_been_guessed(answer_state):
            pass
        else:
            states_guessed.append(answer_state)
            writer.penup()
            writer.goto(int(df[df.state == answer_state].x), int(df[df.state == answer_state].y))
            writer.write(answer_state)
print(missing_states)
writer.goto(0, 300)
writer.write("You win")

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
#

# turtle.mainloop()
