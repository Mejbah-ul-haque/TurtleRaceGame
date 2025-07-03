from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

screen.exitonclick()