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

# create a function to draw the snake
"""
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

# create a function to check if the game is over

"""
check_game_over()
Define the function with no inputs or outputs.
Access the global variables snake_position, window_x, and window_y.
If the x-coordinate of snake_position is less than 0, or greater than 
window_x minus 10, call the game_over() function.
If the y-coordinate of snake_position is less than 0, or greater than 
window_y minus 10, call the game_over() function.

"""

# create a function to check if there is a collision
"""
check_collision()
Define the function with no inputs or outputs.
Access the global variables snake_body and snake_position.
Use a for loop to iterate over each block in snake_body except the first one 
(since the head can't collide with itself).
If the position of the current block matches the position of snake_position, 
call the game_over() function.



"""

# create a function to show the score
"""
show_score()
Define the function with no inputs or outputs.
Access the global variables score, game_window, and white.
Create a font object using pygame.font.SysFont().
Use the render() method on the font object to create a text surface object.
Use the get_rect() method on the text surface object to get a rectangle that 
encloses the text.
Use the blit() method on the game window to display the text surface.


"""
#TODO: No updates have committed to the repository. Student needed to be
# committed to the repo as a contributor