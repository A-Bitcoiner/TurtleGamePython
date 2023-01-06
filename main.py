import turtle

# Set up the game window
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Game")

# Create the maze
maze = turtle.Turtle()
maze.speed(0)
maze.penup()
maze.setposition(-200, -200)
maze.pendown()
maze.pensize(5)

for i in range(4):
    maze.forward(400)
    maze.left(90)

maze.penup()
maze.setposition(0, 0)
maze.pendown()
maze.color("black")

maze.left(90)
maze.forward(50)
maze.right(90)
maze.forward(100)
maze.left(90)
maze.forward(50)
maze.left(90)
maze.forward(100)
maze.right(90)
maze.forward(50)
maze.right(90)
maze.forward(100)

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()

# Set the player's speed
speed = 15

# Define the functions for moving the player
def move_left():
    x = player.xcor()
    x -= speed
    if x < -200:
        x = -200
    player.setx(x)

def move_right():
    x = player.xcor()
    x += speed
    if x > 200:
        x = 200
    player.setx(x)

def move_up():
    y = player.ycor()
    y += speed
    if y > 200:
        y = 200
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= speed
    if y < -200:
        y = -200
    player.sety(y)

# Set up the keybindings
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")

# Keep the window open until the user closes it
wn.listen()
wn.mainloop()
