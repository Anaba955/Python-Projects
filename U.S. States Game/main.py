import turtle
import pandas

screen = turtle.Screen()

# Give background image using turtle library
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_guesses_list = []

while len(correct_guesses_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses_list)}/{len(data)} Correct States",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        all_states = data.state.to_list()
        # list comprehension
        missed_states = [state for state in all_states if state not in correct_guesses_list]
        df = pandas.DataFrame(missed_states)
        df.to_csv("missed_states.csv")
        break
    row = data[data.state == answer_state]
    if not row.empty:
        correct_guesses_list.append(answer_state)
        new_country = turtle.Turtle()
        new_country.hideturtle()
        new_country.penup()
        new_country.goto(int(row.x), int(row.y))
        new_country.write(f"{answer_state}")

# Coordinates are included in csv file
# def get_mouse_click_corr(x, y):
#     """Prints coordinates of mouse when clicked"""
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_corr)
# turtle.mainloop()  # do not exit the screen on click


screen.exitonclick()
