# Import the Pygame library for creating the game
import pygame
# Import the random module for generating random positions for the food
import random

# Initialize Pygame to set up its modules
pygame.init()

# --- Game Window Setup ---
# Set the width of the game window
window_width = 800
# Set the height of the game window
window_height = 600
# Create the game window with the specified dimensions
window = pygame.display.set_mode((window_width, window_height))
# Set the title of the game window
pygame.display.set_caption("Snake Game")

# --- Colors ---
# Define the RGB value for the white color
white = (255, 255, 255)
# Define the RGB value for the black color
black = (0, 0, 0)
# Define the RGB value for the red color
red = (255, 0, 0)

# --- Clock ---
# Create a clock object to control the frame rate of the game
clock = pygame.time.Clock()

# --- Snake Settings ---
# Set the size of each block of the snake
snake_block = 10
# Set the speed of the snake (game update frequency)
snake_speed = 15

# Initialize the font style for displaying text
font_style = pygame.font.SysFont(None, 50)

# Function to display messages on the screen
def display_message(msg, color, x, y):
    """Renders a message and displays it at the given position."""
    # Render the message text with the specified color
    message = font_style.render(msg, True, color)
    # Draw the message on the game window at the specified coordinates
    window.blit(message, [x, y])

# Main game loop function
def game_loop():
    # Flag to indicate if the game is over
    game_over = False
    # Flag to indicate if the game is in the "Game Over" state
    game_close = False

    # --- Snake Initialization ---
    # Set the initial x-coordinate of the snake to the center of the window
    x1 = window_width / 2
    # Set the initial y-coordinate of the snake to the center of the window
    y1 = window_height / 2
    # Initialize the change in x-coordinate (no movement initially)
    x1_change = 0
    # Initialize the change in y-coordinate (no movement initially)
    y1_change = 0

    # Create an empty list to store the snake's body segments
    snake_body = []
    # Set the initial length of the snake to 1 block
    length_of_snake = 1

    # --- Food Initialization ---
    # Generate a random x-coordinate for the food, aligned to the grid
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    # Generate a random y-coordinate for the food, aligned to the grid
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    # Initialize the player's score to 0
    score = 0

    # --- Main Game Loop ---
    while not game_over:
        # --- Game Over Screen ---
        while game_close:
            # Fill the screen with the black color
            window.fill(black)
            # Display a "Game Over" message with options to restart or quit
            display_message("Game Over! Press C to Play Again or Q to Quit", red, window_width / 6, window_height / 3)
            # Update the screen to show the message
            pygame.display.update()

            # Process user input for the "Game Over" screen
            for event in pygame.event.get():
                # If a key is pressed
                if event.type == pygame.KEYDOWN:
                    # Quit the game if the Q key is pressed
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    # Restart the game if the C key is pressed
                    if event.key == pygame.K_c:
                        game_loop()

        # --- Event Handling ---
        for event in pygame.event.get():
            # Exit the game if the user closes the window
            if event.type == pygame.QUIT:
                game_over = True
            # Handle key presses for snake movement
            if event.type == pygame.KEYDOWN:
                # Move left if the LEFT arrow key is pressed and the snake is not moving horizontally
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                # Move right if the RIGHT arrow key is pressed and the snake is not moving horizontally
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                # Move up if the UP arrow key is pressed and the snake is not moving vertically
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                # Move down if the DOWN arrow key is pressed and the snake is not moving vertically
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # --- Snake Movement ---
        # Update the snake's x-coordinate based on the current direction
        x1 += x1_change
        # Update the snake's y-coordinate based on the current direction
        y1 += y1_change

        # --- Boundary Collision Check ---
        # End the game if the snake crosses the window boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # --- Drawing Objects ---
        # Fill the screen with the black color
        window.fill(black)
        # Draw the food as a red square
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])

        # --- Snake Body Update ---
        # Create a list representing the snake's head
        snake_head = [x1, y1]
        # Add the snake's head to its body
        snake_body.append(snake_head)
        # Remove the oldest segment of the snake if it's longer than its current length
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check if the snake collides with itself
        for segment in snake_body[:-1]:
            # End the game if the snake's head collides with any part of its body
            if segment == snake_head:
                game_close = True

        # Draw each segment of the snake's body as a white square
        for segment in snake_body:
            pygame.draw.rect(window, white, [segment[0], segment[1], snake_block, snake_block])

        # --- Display Score ---
        # Render the score text
        score_text = font_style.render("Score: " + str(score), True, white)
        # Display the score at the top-left corner of the screen
        window.blit(score_text, (10, 10))
        # Update the game display with the new score and objects
        pygame.display.update()

        # --- Food Collision Check ---
        # Check if the snake's head is at the same position as the food
        if x1 == foodx and y1 == foody:
            # Generate a new random position for the food
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            # Increase the length of the snake
            length_of_snake += 1
            # Increment the score
            score += 1

        # Control the frame rate of the game based on the snake's speed
        clock.tick(snake_speed)

    # Quit Pygame and close the game window
    pygame.quit()
    # Exit the Python program
    quit()

# Start the game by calling the main game loop
game_loop()
