from turtle import *
def mygoto(x,y):
    up()
    goto(x,y)
    down()
def draw(z):
    begin_fill()
    for i in range(5):
        forward(z)
        right(144)
    end_fill()
setup(700,500,0,0)
color("yellow")
bgcolor("red")
fillcolor("yellow")
hideturtle()
mygoto(-250,75)
draw(100)
mygoto(-130,150)
draw(30)
mygoto(-80,100)
draw(30)
mygoto(-80,40)
draw(30)
mygoto(-130,-10)
draw(30)
down()
