from turtle import Turtle,Screen
from sqlalchemy import create_engine
import pandas

screen=Screen()
screen.setup(800,600)
screen.title("U.S.States")
turtle=Turtle()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states=pandas.read_csv("50_states.csv")
states_list=states["state"].tolist()
guess_num=0
guess_list=[]
game_is=True
while game_is:
    if guess_num!=50:
        answer = screen.textinput(title=f"{guess_num}/50 Guess the state", prompt="What's another state names ?").title()
        guess_num+=1
        if answer=="Exit":
            miss_state=[mis_st for mis_st in states_list if mis_st not in guess_list]
            miss_dict={
                "states":[miss_state]
            }
            new_miss_dict=pandas.DataFrame(miss_state)
            new_miss_dict.to_csv("missing_states.csv")

            break
        if answer in states_list:
            guess_list.append(answer)
            states_grap=states[states["state"]== answer]
            x_vau=int(states_grap["x"])
            y_vau=int(states_grap["y"])

            t=Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x_vau,y_vau)
            t.write(states_grap["state"].item(),align="center")
    else:
        guess_is=False
