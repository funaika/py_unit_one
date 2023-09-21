# Kalen Funai
# 09/21/2023
# Drawing Octagons

import turtle

def drawoctagon(mycolor):

    turtle.color(mycolor)
    turtle.begin_fill()

    for x in range (8):
        turtle.forward(50)
        turtle.left(45)

    turtle.end_fill()

drawoctagon("red")

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(35)
turtle.left(90)

drawoctagon("orange")

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(180)

drawoctagon("purple")

turtle.penup()
turtle.forward(180)

drawoctagon("pink")

turtle.exitonclick()