import turtle
import pandas

tim = turtle.Turtle()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

path = "50_states.csv"
states_data = pandas.read_csv(path)
state_names = states_data["state"].to_list()
# x_coordinates = states_data["x"].to_list()
# y_coordinates = states_data["y"].to_list()

states_dict = states_data.to_dict()
# print(states_dict)
# print(state_names)

answer = screen.textinput(title="Guess The State",
                          prompt="Write the name of the state.").title()

correct_guesses = 0
guesses = []

game_is_on = True
while game_is_on:
    # print(answer)
    if correct_guesses == len(state_names):
        game_is_on = False
    elif answer in state_names and answer not in guesses:
        correct_guesses += 1
        guesses.append(answer)
        ans_index = state_names.index(answer)
        # print(ans_index)
        x_cor = states_dict["x"][ans_index]
        y_cor = states_dict["y"][ans_index]
        # print(x_cor, y_cor)
        tim.hideturtle()
        tim.penup()
        tim.goto(x_cor, y_cor)
        tim.write(answer)

    answer = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                              prompt="What's another state name?").title()
    
    if answer == "Exit":
        '''states_left = []
        #creating states to learn csv file
        for states in state_names:
            if states not in guesses:
                states_left.append(states)'''
        states_left = [states for states in state_names if states not in guesses]
        df = pandas.DataFrame(states_left)
        df.to_csv("states_to_learn.csv")

        game_is_on = False


# Todo: Create a states_to_learn.csv
    

# turtle.mainloop()
# screen.exitonclick()


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
