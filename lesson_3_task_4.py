from turtle import *
t = Turtle()
t.screen.setup(900, 900)
t.up()
t.goto(0, -400)
t.down()
t.fillcolor('yellow')
t.begin_fill() 
t.circle(200,165)
t.up()
t.circle(200,30)
t.down()
t.circle(200,165)
t.end_fill()
t.up()
t.goto(0, -20)
def color_circle(color=str, r=int):
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.up()
color_circle('yellow', 100)
t.goto(0, 80)
t.down()
t.fillcolor('brown')
t.begin_fill() 
t.forward(30)
t.goto(0, 50)
t.goto(-30, 80)
t.forward(30)
t.end_fill()
t.up()
t.goto(35, 100)
color_circle('white', 18)
t.goto(35, 110)
color_circle('black', 6)
t.goto(-35, 100)
color_circle('white', 18)
t.goto(-35, 110)
color_circle('black', 6)
t.goto(200, -200)
t.down()
t.fillcolor('yellow')
t.begin_fill()
t.forward(150)
t.up()
t.left(90)
t.down()
t.circle(100,130)
t.end_fill()
t.up()
t.goto(-200, -200)
t.right(40)
t.down()
t.begin_fill()
t.forward(150)
t.left(90)
t.circle(100,-130)
t.end_fill()
t.up()

