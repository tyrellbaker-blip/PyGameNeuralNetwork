import pygame
import time
import random

# Set the speed of the snake via a variable
speed = 15

# create variables for the window sizes
window_x = 720
window_y = 480

# define the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize Pygame
pygame.init()

# Initialize the game window and set the caption
pygame.display.set_caption("PYTHON - A Snake Game")
game_window = pygame.display.set_mode((720, 480))

# create the frames per second controller with an FPS variable
fps = pygame.time.Clock

# define the default snake position
starting_position = [100, 50]

# create the first 4 blocks of the snake's body
starting_body = [[100, 50],
                 [90, 50],
                 [80, 50],
                 [70, 50]
                 ]

# set the fruit position to a random spot and give it a boolean switch
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# set the default snake position to be moving rightward
direction = "RIGHT"
change_to = direction

# set the initial score to zero
score = 0


# create an event handler function
def handle_events():
    global change_to
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"


# create a function that changes the direction of the snake. Be sure to
# handle double button presses

def change_direction():
    global direction
    global change_to
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"


# create a function to move the snake -- the snake body growing mechanism
# goes here.
"""
spawn_fruit()
Define the function with no inputs or outputs.
Access the global variables fruit_position and fruit_spawn.
Set fruit_position to a list with two elements:
The first element should be a random integer between 1 and window_x//10 (
inclusive), multiplied by 10.
The second element should be a random integer between 1 and window_y//10 (
inclusive), multiplied by 10.
Set fruit_spawn to True.
"""

# create a function to spawn the fruit
"""
DONE
spawn_fruit()
Define the function with no inputs or outputs.
Access the global variables fruit_position and fruit_spawn.
Set fruit_position to a list with two elements:
The first element should be a random integer between 1 and window_x//10 (
inclusive), multiplied by 10.
The second element should be a random integer between 1 and window_y//10 (
inclusive), multiplied by 10.
Set fruit_spawn to True.
"""
def spawn_fruit():
    global fruit_spawn
    global fruit_position
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

# create a function to draw the snake
"""
HELP
draw_snake()
Define the function with no inputs or outputs.
Draw a black rectangle on the game_window using game_window.fill() to clear 
the previous frame.
Use a for loop to iterate over each block in snake_body, and draw a green 
rectangle on game_window using pygame.draw.rect().
Alternatively, you may want to draw an image of the snake instead of 
rectangles.
Draw a white rectangle on game_window using pygame.draw.rect() to represent 
the fruit.
"""
def draw_snake():
    game_window.fill(black)
    for block in starting_body:
        pygame.draw.rect(green)
    for fruit in fruit_position:
        pygame.draw.rect(white)

# create a function to check if the game is over

"""
HELP
check_game_over()
Define the function with no inputs or outputs.
Access the global variables snake_position, window_x, and window_y.
If the x-coordinate of snake_position is less than 0, or greater than 
window_x minus 10, call the game_over() function.
If the y-coordinate of snake_position is less than 0, or greater than 
window_y minus 10, call the game_over() function.
"""
def check_game_over():
    global snake_position
    global window_x
    global window_y
    if snake_position[1] < 0 | snake_position[1] > (window_y - 10):
        #game_over()
    if snake_position[1] < 0 | snake_position[1] > (window_x - 10):
        # game_over()
# create a function to check if there is a collision
"""
DONE
check_collision()
Define the function with no inputs or outputs.
Access the global variables snake_body and snake_position.
Use a for loop to iterate over each block in snake_body except the first one 
(since the head can't collide with itself).
If the position of the current block matches the position of snake_position, 
call the game_over() function.
"""
def check_collision():
    global snake_body
    global snake_position
    for block in snake_body[1:]:
        if snake_position == snake_position[0]:
            #game_over()

# create a function to show the score
"""
DONE
show_score()
Define the function with no inputs or outputs.
Access the global variables score, game_window, and white.
Create a font object using pygame.font.SysFont().
Use the render() method on the font object to create a text surface object.
Use the get_rect() method on the text surface object to get a rectangle that 
encloses the text.
Use the blit() method on the game window to display the text surface.
"""
def show_score():
    global score
    global game_window
    global white
    font = pygame.font.SysFont()
    text = font.render()
    text.get_rect()
    game_window.blit()

# TODO:
#   Thank you so much for these instructions! I just had a few questions on the code
#   since I couldn't figure some stuff out:
#   -----
#   On line 84, the spawn_fruit function is described twice and the function
#   the snake body growing mechanism isn't. I'm not really sure how to write the body
#   growing function.
#   -----
#   Also, should there be a separate game_over() function? Or is there already
#   one built in? I don't see the instructions to make it, so I was wondering.
#   -----
#   Lastly, when is says snake_position in line 146, was that supposed to be
#   declared in the beginning? I checked and saw I never had a variable called that.
#   -----
#   Can you please check the other function in my code to make sure they are correct?
#   Thanks!