import turtle
size = int(input("Please input size:(20~200)"))

t = turtle.Turtle()
t.color('blue')
t.pensize(5)

for i in range (5):
    t.forward(size)
    t.right(144)

t.hideturtle()
turtle.done()
