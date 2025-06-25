import numpy as np
import random 

# Import functions from game_of_life.py for board creation and rendering
from game_of_life import random_state, render, dead_state, get_board_dimensions # Ensure all needed functions are here

from ga_solver import select_parents, crossover, create_initial_population, calculate_fitness # Include create_initial_population and calculate_fitness for generating dummy data

# --- Test Parameters (can be adjusted) ---
TEST_POP_SIZE = 10
TEST_BOARD_WIDTH = 5
TEST_BOARD_HEIGHT = 5
TEST_TOURNAMENT_SIZE = 3 # A small tournament size for testing selection

print("="*50)
print("--- Testing Genetic Algorithm Operations ---")
print("="*50 + "\n")

# --- PART 1: Test select_parents ---
print("\n--- Testing select_parents ---")

# Create a small dummy population
dummy_population = create_initial_population(TEST_POP_SIZE, TEST_BOARD_WIDTH, TEST_BOARD_HEIGHT)

# Create dummy fitness scores for the population
dummy_fitnesses = [random.randint(1, 20) for _ in range(TEST_POP_SIZE)]

print(f"Dummy Population Size: {len(dummy_population)}")
print(f"Dummy Fitness Scores: {dummy_fitnesses}\n")

# Pair population with fitnesses to see the scores
for i, (individual, fitness) in enumerate(zip(dummy_population, dummy_fitnesses)):
    print(f"Individual {i+1} (Fitness: {fitness}):")
    render(individual) 

# Select Parent 1
print("\nSelecting Parent 1:")
parent1_selected = select_parents(dummy_population, dummy_fitnesses, TEST_TOURNAMENT_SIZE)
print("Parent 1 (selected) initial state:")
render(parent1_selected)

# Select Parent 2 (make sure it's potentially different from Parent 1 for good crossover)
print("\nSelecting Parent 2:")
parent2_selected = select_parents(dummy_population, dummy_fitnesses, TEST_TOURNAMENT_SIZE)

print("Parent 2 (selected) initial state:")
render(parent2_selected)

print("\n--- select_parents test complete ---\n")

# --- PART 2: Test crossover ---
print("--- Testing crossover ---")

# Create two distinct dummy parent boards for clear observation of mixing
dummy_parent1 = np.array([
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
], dtype=int) # Checkerboard pattern

dummy_parent2 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1], # Solid line in the middle
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
], dtype=int) # Horizontal line in middle

print("\nRaw Dummy Parent 1:")
print(dummy_parent1) # This is what I added to help me find my zombie bug
print("\nRendered Dummy Parent 1:")
render(dummy_parent1)

print("\nRaw Dummy Parent 2:")
print(dummy_parent2) # This is what I added to help me find my zombie bug
print("\nRendered Dummy Parent 2:")
render(dummy_parent2)

# Perform crossover
child1, child2 = crossover(dummy_parent1, dummy_parent2)

print("\n--- Observing Crossover Mixing ---")
print("Raw Child 1:")
print(child1) # This is what I added to help me find my zombie bug
print("\nRendered Child 1:")
render(child1)

print("\nRaw Child 2:")
print(child2) # This is what I added to help me find my zombie bug
print("\nRendered Child 2:")
render(child2)

print("\nObservation Notes for Crossover:")
print("- Compare each cell in Child 1 and Child 2 to the corresponding cells in Parent 1 and Parent 2.")
print("- For each cell, Child 1 should either match Parent 1 (and Child 2 matches Parent 2), OR")
print("- Child 1 should match Parent 2 (and Child 2 matches Parent 1). This shows the 50% swap.")
print("- Run this script multiple times to see different mixing patterns due to randomness.")

print("\n--- crossover test complete ---")

print("\n" + "="*50)
print("--- All GA Operations Tests Complete ---")
print("="*50)