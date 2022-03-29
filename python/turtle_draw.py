#Drawing using turtle 
import turtle
melinda=turtle.Turtle()
melinda.color("gray")
melinda.forward(100)
melinda.left(120)
melinda.forward(100)
melinda.left(12/2)
melinda.forward(100)

# practice drawing a square using turtle.
import turtle
amy = turtle.Turtle()
amy.color("red")
for sides in [1,2,3,4]:
    amy.forward(100)
    amy.right(90)
    amy.forward(100)
    amy.right(90)

# Proper commentation

# Import the turtle module.
import turtle

# Create a new turtle named amy.
amy = turtle.Turtle()

# Set amy's color.
amy.color("yellow")

# Have amy draw a square
amy.forward(100)
amy.right(90)
amy.forward(100)
amy.right(90)
amy.forward(100)
amy.right(90)
amy.forward(100)


# multple color square 
#imports package
import turtle
# assigns a variable to command
mary = turtle.Turtle()
#color assignment
lovely_colour="purple"
color="yellow"
color2="pink"
#draws the image 
mary.color(color)
mary.forward(100)
mary.right(90)
mary.color(color2)
mary.forward(100)
mary.right(90)
mary.color(lovely_colour)
mary.forward(100)
mary.right(90)
mary.color("black")
mary.forward(100)

#creating a chain from turtles
import turtle

links = [1, 2, 3, 4, 5, 6, 7, 8]
sides = [1, 2, 3, 4, 5, 6]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(0)
weaver.pendown()

for link in links:
    # Draw a hexagon.
    for side in sides:
        weaver.forward(100)
        weaver.right(60)

    # Scoot over to the next link.
    weaver.penup()
    weaver.left(0)
    weaver.forward(60)
    weaver.pendown()

weaver.hideturtle()

# changes lines in different colours and introduces space within them 
import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see

amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(70)
# Draw a red line
amy.pendown()
amy.color("red")
amy.forward(50)

# Move forward without drawing anything
amy.penup()
amy.forward(50)

# Draw an orange line
amy.pendown()
amy.color("orange")
amy.forward(50)

# Move forward without drawing anything
amy.penup()
amy.forward(50)

# Draw a yellow line
amy.pendown()
amy.color("yellow")
amy.forward(50)
# checks the loop of python code 
import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three red lines, with space in between
amy.color("red")
for line in [1,2,3]:
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()

#used for drawing lines with different colours using for loop
import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.forward(-140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
  amy.color(prettycolor)
  amy.forward(50)
  amy.penup()
  amy.forward(50)
  amy.pendown()

  ## ASSIGNMENT FOR ONE 

# Write whatever code you want here!

    
#used for drawing lines with different colours using for loop
import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.forward(-140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for rainbow in ["red", "orange", "yellow", "green", "blue", "purple"]:
  amy.color(rainbow)
  amy.forward(50)
  amy.right(60)
  amy.penup()
  amy.forward(0)
  amy.pendown()

  # Drawing multicoloured stars
import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Write whatever code you want here!
stars = turtle.Turtle()
stars.width(5)
stars.speed(0)
for color in rainbow:
    stars.color(color)
    for side in [1, 2, 3, 4, 5]:
        stars.forward(50)
        stars.right(144)
    stars.right(60)
    stars.penup()
    stars.forward(50)
    stars.pendown()

# Draws the circle 
import turtle

# Let's draw a hundred-sided polygon!
# But this way is silly ...
sides = range(100)

t = turtle.Turtle()
t.color("magenta")
t.width(5)

for side in sides:
    t.forward(5)
    t.right(360 / 100)

# Rewrite the above code to use range().
# (When you're done you should be able
# to delete the giant list!)

# creating your own function
import turtle

def spiral():
    t = turtle.Turtle()
    t.color("cyan")
    for n in range(100):
        t.forward(n)
        t.right(20)

spiral()

# Draw multiple square
import turtle
def draw_square(sides,color,angle,length):
    jack = turtle.Turtle()
    jack.color(color)
    for side in range(sides):
        jack.forward(length)
        jack.right(angle)
        jack.hideturtle()
        
draw_square( 4, "cyan", 90, 100)
draw_square(4, "cyan", 90, 50)
draw_square(4, "cyan", 90, 25)

#using romeo and juliet to describe if function
import turtle

romeo = turtle.Turtle()
juliet = turtle.Turtle()

juliet.color("misty rose")
juliet.width(3)

romeo.color("violet")
romeo.width(3)

romeo_last_name = "montague"

romeo.left(40)
romeo.forward(100)
for side in range(185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()

juliet.left(140)
juliet.forward(100)
for side in range(185):
    juliet.forward(1)
    juliet.right(1)
    juliet.hideturtle()

# modulo challenges 
# This program draws a string of beads.
# Change it so that the beads' colors
# alternate:  red, blue, red, blue ...

import turtle

def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)

t = turtle.Turtle()
t.speed(0)
t.width(2)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

# Draw ten beads.
for n in range(10):
    if n % 2== 0:
        t.color("blue")
    else:
        t.color("red")
    bead(t)
    t.forward(40)

# staircase 
# Write code to draw the staircase
# pattern above.  The modulo operation
# might be useful!

#drawing a stair case
#import package
import turtle
joy=turtle.Turtle()
joy.width(5)
# dimension of a stair case
joy.color("green")
for line in range(12):
    joy.forward(10)
    if line % 2 == 0:
        joy.right(90)
    else:
        joy.left(90)
joy.hideturtle()

import turtle

def fizz(tur):
    # A red square bead.
    tur.color("red")
    tur.left(90)
    for side in [10, 20, 20, 20, 10]:
        tur.forward(side)
        tur.right(90)
# fizzbuzz challenge

def buzz(tur):
    # A green hexagonal bead.
    # Fits inside the red bead.
    tur.color("green")
    tur.left(60)
    for side in range(6):
        tur.forward(10)
        tur.right(60)
    tur.right(60)
def plain(tur):
    # A gray octagonal bead.
    tur.color("gray")
    tur.left(90)
    for side in [4, 8, 8, 8, 8, 8, 8, 8, 4]:
        tur.forward(side)
        tur.right(45)
    tur.right(45)

# Set up the turtle to draw beads.
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.penup()
t.back(180)  # Back up to make room!
t.pendown()

for num in range(16):
    # Change this code:
    if num % 3 ==0:
        fizz(t)
    if num % 5 == 0:
        buzz(t)
    if num % 3 != 0 and num %5 != 0:
        plain(t)
  # Advance to the next bead spot.
    t.color("gray")
    t.forward(22)
t.hideturtle()

 