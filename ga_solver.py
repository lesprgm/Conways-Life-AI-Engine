import numpy as np
from game_of_life import(next_board_state, random_state, random)
from ga_parameters import *

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
            
def mutation(individual, mutation_rate):
    mutated_individual = individual.copy()
    board_height, board_width = individual.shape

    for y in range(board_height):
        for x in range(board_width):
            if random.random() < mutation_rate:
                mutated_individual[y, x] = 1 - mutated_individual[y, x]
    return mutated_individual

def evolve_patterns():
    
    #population = create_initial_population(pop_size, board_width, board_height)
    population = create_initial_population(ga_population_size, ga_board_width, ga_board_height)

    
    best_individual = None
    best_fitness = -1
    fitness_history = []
    for generation in range(ga_num_generations):
        print(f" Generation {generation + 1}/{ga_num_generations} ")
        fitnesses = []
        for i, individual in enumerate(population):
            fitness = calculate_fitness(individual, ga_simulation_steps)
            fitnesses.append(fitness)
        current_best_fitness_index = np.argmax(fitnesses)
        current_best_fitness = fitnesses[current_best_fitness_index]
        current_best_individual = population[current_best_fitness_index]
        
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_individual = current_best_individual.copy()
        
        fitness_history.append(current_best_fitness)
        if best_fitness >= ga_fitness_threshold:
            break
        
        next_population = []
        for _ in range(ga_population_size // 2):
            parent1 = select_parents(population, fitnesses, ga_tournament_size)
            parent2 = select_parents(population, fitnesses, ga_tournament_size)
            
            if random.random() < ga_crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1.copy(), parent2.copy()
                
            mutated_child1 = mutation(child1, ga_mutation_rate)
            mutated_child2 = mutation(child2, ga_mutation_rate)
            
            next_population.append(mutated_child1)
            next_population.append(mutated_child2)
            
        population = next_population

        print("-" * (40) + "\n")
        
    print(f"\nGA finished after {generation + 1} generations.")
    print(f"Final best overall fitness: {best_fitness}")
    return best_individual, fitness_history
    