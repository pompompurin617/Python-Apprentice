"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600, startx=0, starty=0)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.left(90)
# Use tina.forward(20) and tina.left(90) to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()
tina.forward(40)
tina.left(90)
tina.forward(40)
tina.left(90)
tina.forward()


... # Your code here tina. forward (90)

turtle.exitonclick()                    # Close the window when we click on it
