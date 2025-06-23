import numpy as np
from game_of_life import(next_board_state, random_state)

def calculate_fitness ( board, num_simulation_steps):
    current_sim_board = board.copy()
    previous_sim_board = None
    for generation in range(1, num_simulation_steps + 1):
        next_sim_board = next_board_state(current_sim_board)
        
        if not next_sim_board.any():
            return generation 
        if previous_sim_board is not None and np.array_equal(next_sim_board, previous_sim_board):
            return generation
        previous_sim_board = current_sim_board.copy()
        current_sim_board = next_sim_board.copy()
    return num_simulation_steps
    
def create_initial_population(population_size, width, height):
    population =[]
    for _ in range(population_size):
        individual_board = random_state(width, height)
        population.append(individual_board)
    return population 