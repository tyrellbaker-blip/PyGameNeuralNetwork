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



"""

# create a function to spawn the fruit
"""



"""

# create a function to draw the snake
"""



"""

# create a function to check if the game is over

"""


"""

# create a function to check if there is a collision

# create a function to show the score
