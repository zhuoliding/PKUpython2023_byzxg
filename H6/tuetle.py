n = float(input('How long is the tranigle?'))
import turtle
import math
t = turtle.Turtle()
t.pencolor('black')
t.pensize(n/15)
t.fillcolor('yellow')
t.up()
t.goto(-n/2,-n/6*math.sqrt(3))
t.down()
t.begin_fill()
t.forward(n)
t.left(120)
t.forward(n)
t.left(120)
t.forward(n)
t.end_fill()
t.up()
t.goto(0,-n/12*math.sqrt(3))
t.down()
t.pensize(n/20)
t.dot()
t.up()
t.goto(0,-n/20)
t.fillcolor('black')
t.pensize(n/1000)
t.down()
t.begin_fill()
t.goto(n/20,n/7*math.sqrt(3))
t.seth(90)
t.circle(n/20,180)
t.goto(0,-n/20)
t.end_fill()








t.hideturtle()
turtle.done()