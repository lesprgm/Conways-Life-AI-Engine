import numpy as np
import pygame 
import time
import matplotlib.pyplot as plt
from game_of_life import *
from ga_solver import *
from ga_parameters import *

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
            
def plot_ga_results(history):
    plt.plot(history)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('GA Fitness over generations')
    plt.show()
    
    
    
if __name__ == "__main__":
    evolved_pattern, fitness_history = evolve_patterns()
    
    plot_ga_results(fitness_history)
    
    print("\n--- Verifying Evolved Pattern for Pygame ---")
    print(f"Type of evolved_pattern: {type(evolved_pattern)}")
    print(f"Shape of evolved_pattern: {evolved_pattern.shape}")
    print("Content of evolved_pattern (INITIAL state, before Pygame sim starts):")
    render(evolved_pattern) 

    actual_fitness_of_displayed_pattern = calculate_fitness(evolved_pattern, ga_simulation_steps)
    print(f"Actual fitness of this specific pattern (as per calculate_fitness): {actual_fitness_of_displayed_pattern}")
    print("------------------------------------------\n")
    
    pygame.init()

    board_height ,board_width = evolved_pattern.shape

    scree_width = board_width * cell_size
    screen_height = board_height * cell_size
    
    screen = pygame.display.set_mode((scree_width, screen_height))

    pygame.display.set_caption("Conway's Game of Life Test")
    
    current_board_state = evolved_pattern.copy()


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