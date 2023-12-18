import time
import turtle

t = turtle.Turtle()
t.up()
t.goto(-100,100)
t.down()
t.speed(0)

# campo de carrera
for i in range(15):
    t.write(i)
    t.right(90)
    t.forward(200)
    t.left(180)  
    t.forward(200)
    t.right(90)
    t.forward(20)
first = turtle.Turtle()
first.shape("turtle")
first.color("red")
first.up()
first.goto(-120,70)
first.down()

second = turtle.Turtle()
second.shape("turtle")
second.color("blue")
second.up()
second.goto(-120,40)
second.down()

third = turtle.Turtle()
third.shape("turtle")
third.color("yellow")
third.up()
third.goto(-120,10)
third.down()

time.sleep(10)