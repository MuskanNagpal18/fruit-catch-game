
import turtle
import random
import time

wn = turtle.Screen()
wn.title("Fruit Catch Game - by Roshni")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)
wn.tracer(0)

basket = turtle.Turtle()
basket.shape("square")
basket.color("brown")
basket.shapesize(stretch_wid=1, stretch_len=4)
basket.penup()
basket.goto(0, -250)

fruits = []
colors = ["red", "orange", "yellow", "purple", "pink"]
for _ in range(5):
    f = turtle.Turtle()
    f.shape("circle")
    f.color(random.choice(colors))
    f.penup()
    f.goto(random.randint(-250, 250), random.randint(100, 600))
    fruits.append(f)

score = 0
missed = 0
speed = 2
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("darkblue")
score_display.goto(0, 260)
score_display.write(f"Score: {score} Missed: {missed}", align="center", font=("Comic Sans MS", 18, "bold"))

def move_left():
    x = basket.xcor() - 30
    if x > -250:
        basket.setx(x)

def move_right():
    x = basket.xcor() + 30
    if x < 250:
        basket.setx(x)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

game_on = True
while game_on:
    wn.update()
    time.sleep(0.02)
    for f in fruits:
        f.sety(f.ycor() - speed)
        if f.ycor() < -280:
            f.goto(random.randint(-250, 250), random.randint(400, 700))
            missed += 1
        if f.distance(basket) < 40 and f.ycor() > -260:
            f.goto(random.randint(-250, 250), random.randint(400, 700))
            score += 1
            speed += 0.02
    score_display.clear()
    score_display.write(f"Score: {score} Missed: {missed}", align="center", font=("Comic Sans MS", 18, "bold"))
    if missed >= 5:
        game_on = False

score_display.goto(0, 0)
score_display.color("red")
score_display.write(f"GAME OVER!\nFinal Score: {score}", align="center", font=("Comic Sans MS", 22, "bold"))
wn.mainloop()

