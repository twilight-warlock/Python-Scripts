import turtle
import time
import random

delay = 0.1
segments = []

# Game screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("#a2d5c6")
window.setup(600, 600)
window.tracer(0)

# Snake Head (initial snake)
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#077b8a")
head.penup()
head.goto(0, 100)
head.direction = "stop"


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#d72631")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# Score
score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}".format(high_score),
          align="center", font=("Courier", 24, "normal"))

# Movement


def move():
    if head.direction == "up":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()  # x coordinate of the turtle
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Rules
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


# Input keyboard key bindings
window.listen()
window.onkey(go_up, "w")
window.onkey(go_up, "Up")
window.onkey(go_down, "s")
window.onkey(go_down, "Down")
window.onkey(go_right, "d")
window.onkey(go_right, "Right")
window.onkey(go_left, "a")
window.onkey(go_left, "Left")


# To keep window open and update the main game
while True:
    window.update()
    move()
    time.sleep(delay)
    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        if len(segments) == 0:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color("#077b8a")
            new_segment.penup()
            segments.append(new_segment)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("#5c3c92")
        new_segment.penup()
        segments.append(new_segment)
        score = score+10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("score: {} High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        # clear segment list
        segments = []
        score = 0
        pen.clear()
        pen.write("score: {} High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    # Check for head collision
    for i in range(len(segments)-1, 1, -1):
        if segments[i].distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments = []
            score = 0
            pen.clear()
            pen.write("score: {} High Score: {}".format(
                score, high_score), align="center", font=("Courier", 24, "normal"))
