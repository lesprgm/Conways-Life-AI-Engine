import numpy as np
import pygame 
import time
from game_of_life import(
    dead_state,
    random_state,
    next_board_state,
    get_board_dimensions,
    render
)

alive = "green"
dead = "black"

cell_size = 12     

def draw_board_pygame(screen, board_state, cell_size):
    board_height, board_width = board_state.shape
    for y in range(board_height):
        for x in range(board_width):
            cell_value = board_state[y, x]
            x_pixel = x * cell_size
            y_pixel = y * cell_size
            color = alive if cell_value == 1 else dead
            pygame.draw.rect(screen, color, (x_pixel, y_pixel, cell_size, cell_size))
    
    
if __name__ == "__main__":
    pygame.init()

    board_width = 30
    board_height = 30

    scree_width = board_width * cell_size
    screen_height = board_height * cell_size
    
    screen = pygame.display.set_mode((scree_width, screen_height))

    pygame.display.set_caption("Conway's Game of Life Test")
    
    current_board_state = random_state(board_width, board_height)


    running = True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        screen.fill(dead)
        draw_board_pygame(screen, current_board_state, cell_size) 

        pygame.display.update() 
        
        current_board_state = next_board_state(current_board_state)
        time.sleep(0.1)

    pygame.quit()
    print("Pygame window closed.")