from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()
tim.speed("slowest")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def setheading_counter_clockwise():
    tim.left(10)

def setheading_clockwise():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(setheading_counter_clockwise, "a")
screen.onkey(setheading_clockwise, "d")
screen.onkey(clear_screen, "c")



screen.exitonclick()