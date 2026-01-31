import turtle

# creating canvas
# You can combine these:
sc = turtle.Screen()
sc.bgcolor("Orange")
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
    board.forward(100)
    board.left(90)
    # Note: In Python, 'i' increments automatically in a range loop, 
    # so 'i = i + 1' isn't needed here.

# THE MISSING LINE:
turtle.done()