from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ['purple','blue','green','yellow','orange','red']
user_bet = screen.textinput(title="Make you bet",prompt="which turtle will win the race? Enter a color: ")
y_pos = [-100,-60,-20,20,60,100]
all_turtles = []
for i in range(6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[i])
    tim.goto(x = -230,y = y_pos[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} is the winner ")    
        distance = random.randint(0,10) 
        turtle.forward(distance) 

screen.exitonclick()


