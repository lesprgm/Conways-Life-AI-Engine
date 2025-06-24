import numpy as np
from game_of_life import(next_board_state, random_state, random)

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

def select_parents(population, fitness, tournament_size):
    participants = random.sample(list(zip(population, fitness)),tournament_size)
    parent = max(participants, key= lambda x: x[1])
    return parent[0]

def crossover(parent1, parent2):
    board_height, board_width = parent1.shape
    child1 = np.zeros((board_height, board_width), dtype = int)
    child2 = np.zeros((board_height, board_width), dtype = int)
    
    for y in range(board_height):
        for x in range(board_width):
            if random.random() < 0.5:
                child1[y, x] = parent1[y, x]
                child2[y, x] = parent2[y, x]
            else:
                child2[y, x] = parent1[y, x]
                child1[y, x] = parent2[y, x]
    return child1, child2
            
    