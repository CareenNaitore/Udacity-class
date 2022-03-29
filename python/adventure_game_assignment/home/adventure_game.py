# import packages

import time
import random
import turtle

# Assigning variables in random

enemies = ['Genie', 'fairies', 'witches']
enemy = random.choice(enemies)
jewels = ['lamp', 'diamond', 'sapphire']
jewel = random.choice(jewels)

# Function for printing


def print_pause(message, time_waiting):
    print(message)
    time.sleep(time_waiting)

# Function for printing introduction to the game


def intro():
    print_pause("As you are stambling through the forest", 2)
    print_pause("you meet a little girl walking with a basket", 2)
    print_pause("she asks  you if you would like to engage in an adventure", 2)
    choice = input("would you take \n(1)An adventure\n(2)Go home\n")
    if choice == '1':
        print_pause("run into the forest", 2)
        print_pause("you come across a cave...", 1)
        print_pause("Therefore,your adventure begins you enter the cave.", 2)
        print_pause("you come across a ruby guided by troll.", 2)
        print_pause("you take the jewel and troll offers you one wishes", 2)
        choices = input("you have three choices (a)wealth,(b)health,(c)love\n")
        if choices == 'a':
            print_pause("you live a luxurious life with no love and health", 2)
            print_pause("until  you last days.", 2)
        if choices == 'b':
            print_pause("A long and healthy life without money and love", 2)
            print_pause("but you died at an old age", 2)
        if choices == 'c':
            print_pause("health and wealth accompany love", 2)
            print_pause("A long,healthy and wealthy life with love", 2)
    elif choice == '2':
        print_pause("you walk towards your house ", 2)
        print_pause("reaching your house", 3)
        print_pause("you go to bed", 2)


intro()

# create images for the end of the games


def image():
    cat = turtle.Turtle()
    cat.write("Thank you for playing the game", font=("Verdana", 20, "normal"))
    cat.hideturtle()
    romeo = turtle.Turtle()
    juliet = turtle.Turtle()
    romeo.speed(0)
    juliet.speed(0)
    juliet.color("red")
    juliet.width(3)
    romeo.color("red")
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

# Function for playing again


def play_again():
    choice = ''
    while choice not in ['yes', 'no']:
        choice = input("would you prefer playing again (yes/no)\n")
        if choice == 'no':
            image()
            return exit()
        elif choice == 'yes':
            print_pause("congratulation, lets play again ...", 2)
            return 'running'


play_again()

# Function for the house


def house():
    print_pause("you walk towards your house ", 2)
    print_pause("Reaching your house", 3)
    print_pause("you go to bed", 2)

# Function for the cave


def cave():
    print_pause("run into the forest", 2)
    print_pause("you come across a cave...", 1)
    print_pause("your adventure begins you enter the cave.", 2)
    print_pause(f"you come across a {jewel} guided by {enemy}.",  2)
    print_pause(f"you take the {jewel} and {enemy} offers you one wishes", 2)
    choices = input("you have 3 choices (a)wealth, (b)health, (c)love\n")
    if choices == 'a':
        print_pause("A luxurious life with no love and health", 2)
        print_pause("until  you last days.", 2)
    if choices == 'b':
        print_pause("A long and healthy life without money and love", 2)
        print_pause("but you died at an old age", 2)
    if choices == 'c':
        print_pause("health and wealth accompany love", 2)
        print_pause("A long,healthy and wealthy life with love", 2)

# Function for the cave


def where_to():
    print_pause("", 1)
    print_pause("Enter 1 to go to the house.", 2)
    print_pause("Enter 2 to go to the cave.", 2)
    print_pause("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        house()
    elif choice == '2':
        cave()


where_to()

# end of the game

game_state = 'running'
while game_state == 'running':
    play_again()
    where_to()


gamestate = play_again()
