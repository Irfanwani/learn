from turtle import *


wn = Screen()
wn.setup(600, 600)

# creating playground
pg = Turtle()
pg.speed(0)
pg.penup()
pg.goto(250, 250)
pg.pendown()
for i in range(4):
    pg.right(90)
    pg.forward(500)
pg.hideturtle()

# create paddles as players
paddle1 = Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.penup()
paddle1.shapesize(5, 1)
paddle1.goto(-240, 0)

paddle2 = Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.penup()
paddle2.shapesize(5, 1)
paddle2.goto(240, 0)

# adding ball to the game
ball = Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("teal")


def firstup():
    y = paddle1.ycor()
    if y < 200:
        paddle1.sety(y + 10)


def firstdown():
    y = paddle1.ycor()
    if y > -200:
        paddle1.sety(y - 10)


def secondup():
    y = paddle2.ycor()
    if y < 200:
        paddle2.sety(y + 10)


def seconddown():
    y = paddle2.ycor()
    if y > -200:
        paddle2.sety(y - 10)


wn.onkey(firstup, "w")
wn.onkey(firstdown, "d")

wn.onkey(secondup, "Up")
wn.onkey(seconddown, "Down")
wn.listen()

xin = 1
yin = 1

# score counters
score1 = 0
score2 = 0

pen1 = Turtle()
pen1.speed(0)
pen1.penup()
pen1.goto(-260, 260)
pen1.hideturtle()
pen1.write(f'Score1: {score1}')

pen2 = Turtle()
pen2.speed(0)
pen2.penup()
pen2.goto(240, 260)
pen2.hideturtle()
pen2.write(f'Score2: {score2}')

while True:
    x = ball.xcor()
    y = ball.ycor()
    ball.goto(x+xin, y+yin)

    if y >= 240:
        yin = -1
    
    if y <= -240:
        yin = 1

    
    if x <= paddle1.xcor() + 20 and x >= paddle1.xcor() and y <= paddle1.ycor() + 50 and y >= paddle1.ycor() - 50:
        xin = 1
        score1 += 1
        pen1.clear()
        pen1.write(f'Score1: {score1}')
    if x >= paddle2.xcor() - 20 and x <= paddle2.xcor() and y <= paddle2.ycor() + 50 and y >= paddle2.ycor() - 50:
        xin = -1
        score2 += 1
        pen2.clear()
        pen2.write(f'Score2: {score2}')


    if x >= 240 or x <= -240:
        ball.goto(0, 0)
        break

    
wn.mainloop()
