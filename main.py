import turtle

def draw_maze(t, maze):
    for row in maze:
        for col in row:
            if col == "S":
                t.color("green")
            elif col == "E":
                t.color("red")
            elif col == "X":
                t.color("black")
            else:
                t.color("white")
            t.stamp()
            t.forward(20)
        t.backward(20 * len(row))
        t.right(90)
        t.forward(20)
        t.left(90)

def create_maze(maze):
    t = turtle.Turtle(shape="square")
    t.shapesize(0.5, 0.5, 2)
    t.speed(0)
    t.penup()
    x, y = -250, 250
    t.goto(x, y)
    draw_maze(t, maze)

def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

def setup_controls():
    turtle.listen()
    turtle.onkey(move_up, "Up")
    turtle.onkey(move_down, "Down")
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")
def create_player():
    t = turtle.Turtle(shape="circle")
    t.color("blue")
    t.penup()
    t.speed(0)
    return t

maze = [
    ["S", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"],
    ["X", " ", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X"],
    ["X", " ", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X"],
    ["X", " ", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
    ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", "E"],
]

create_maze(maze)
player = create_player()
setup_controls()

turtle.exitonclick()
