import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Snake settings
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)


def display_message(msg, color, x, y):
    """Displays a message on the screen."""
    message = font_style.render(msg, True, color)
    window.blit(message, [x, y])


def game_loop():
    game_over = False
    game_close = False

    # Snake starting position
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    snake_body = []
    length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    score = 0

    while not game_over:

        while game_close:
            window.fill(black)
            display_message("Game Over! Press C to Play Again or Q to Quit", red, window_width / 6, window_height / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Check for boundary collision
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])

        # Update snake body
        snake_head = [x1, y1]
        snake_body.append(snake_head)
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check if the snake hits itself
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        for segment in snake_body:
            pygame.draw.rect(window, white, [segment[0], segment[1], snake_block, snake_block])

        # Display score
        score_text = font_style.render("Score: " + str(score), True, white)
        window.blit(score_text, (10, 10))
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
