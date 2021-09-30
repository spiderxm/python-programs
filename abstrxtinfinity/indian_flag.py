import turtle

t = turtle.Turtle()


def rectangle(color):
    t.pendown()
    t.pensize(1)
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(200)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.penup()


def circle(color, radius):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.circle(-radius)
    t.setheading(270)
    t.penup()
    t.forward(radius)
    t.setheading(0)
    t.pendown()
    for i in range(24):
        t.forward(radius - 2)
        t.bk(radius - 2)
        t.left(15)


t.penup()
t.goto(0, -100)
t.pendown()
t.pensize(12)
t.color("brown")
t.pendown()

t.goto(0, 200)
t.color("black")
rectangle("orange")

t.goto(0, 150)
rectangle("white")

t.goto(0, 100)
rectangle("green")

t.goto(100, 145)
circle("blue", 20)

t.hideturtle()
ts = turtle.getscreen()
turtle.getcanvas().postscript(file="flag.mp4")

turtle.exitonclick()
