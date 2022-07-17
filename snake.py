from time import sleep
from turtle import *
from random import choice, randint


wn = Screen()
wn.setup(600, 600)
wn.bgcolor("grey")

# random shape generator function
def shp():
    s = choice(["square", "triangle", "circle"])
    return s


# random color generator function
def clr():
    c = choice(["green", "red", "blue", "orange", "pink", "violet"])
    return c


score = 0

# writing score to the screen
writer = Turtle()
writer.speed(0)
writer.penup()
writer.goto(-270, 270)
writer.hideturtle()
writer.write(f"Score: {score}")

# writing alert messages
pen = Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(-100, 0)


# Creating a table for the game
pg = Turtle()
pg.speed(0)
pg.penup()
pg.goto(250, 250)
pg.pendown()
for i in range(4):
    pg.right(90)
    pg.forward(500)
pg.hideturtle()


# creating food for the snake
food = Turtle()
food.speed(0)
food.penup()
food.shape(shp())
food.color(clr())
food.goto(randint(-240, 240), randint(-240, 240))

# creating the head of the snake
head = Turtle()
head.speed(0)
head.penup()
head.shape("square")
head.color("orange")
head.direction = "Stop"

# adding functions for movement on keypresses
def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goright():
    if head.direction != "left":
        head.direction = "right"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def gameOver():
    if (
        head.xcor() <= -240
        or head.xcor() >= 240
        or head.ycor() <= -240
        or head.ycor() >= 240
    ):
        pen.write("GAME OVER! Press R To restart", font=30)
        return True
    return False


def restart():
    global score
    head.goto(0, 0)
    food.goto(randint(-240, 240), randint(-240, 240))
    pen.clear()
    score *= 0
    writer.clear()
    writer.write(f"Score: {score}")
    mainGame()


wn.listen()
wn.onkey(goup, "Up")
wn.onkey(godown, "Down")
wn.onkey(goright, "Right")
wn.onkey(goleft, "Left")
wn.onkey(restart, "r")


def mainGame():
    global score
    blocks = []
    while True:
        wn.update()

        if head.distance(food) < 20:
            food.color(clr())
            food.shape(shp())
            food.goto(randint(-240, 240), randint(-240, 240))
            score += 10
            writer.clear()
            writer.write(f"Score: {score}")

            tail = Turtle()
            tail.speed(0)
            tail.penup()
            tail.shape("square")
            tail.color("green")
            blocks.append(tail)

        hx = head.xcor()
        hy = head.ycor()

        if len(blocks) > 0:
            for i in range(1, len(blocks)):
                x = blocks[i - 1].xcor()
                y = blocks[i - 1].ycor()

                blocks[i].goto(x, y)

            blocks[0].goto(hx, hy)

        if gameOver():
            [block.goto(1000, 1000) for block in blocks]
            blocks = []
            break

        move()

        sleep(0.05)


mainGame()
wn.mainloop()
