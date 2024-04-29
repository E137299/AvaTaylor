import turtle
import random

# Function to draw text
def draw_text(text, font_size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.write(text, align="center", font=("Arial", font_size, "normal"))

# Function to draw a firework pattern
def draw_firework(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(36):
        turtle.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
        turtle.forward(100)
        turtle.backward(100)
        turtle.left(10)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")



turtle.speed(0)
turtle.hideturtle()

# Draw text
draw_text("Congratulations Ava!\nGood Luck at St. Ed's.", 20, 0, 100)

# Draw multiple firework patterns
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    draw_firework(x, y)

turtle.done()
