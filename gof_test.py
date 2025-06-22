# test.py
import numpy as np

# To import from game_of_life.py, ensure both files are in the same directory.
# If not, you might need to adjust your PYTHONPATH or use a more advanced import structure.
# For simplicity, we'll assume they are in the same directory.
from game_of_life import next_board_state, dead_state, random_state, render, get_board_dimensions
from ga_solver import calculate_fitness

# Helper function to run a single test case for next_board_state
def run_test(test_name, initial_state_list, expected_next_state_list):
    """
    Runs a single test case for next_board_state and prints the result.
    Converts input lists to NumPy arrays for compatibility with refactored functions.
    """
    # Convert input lists to NumPy arrays for the refactored next_board_state function
    initial_state = np.array(initial_state_list, dtype=int)
    expected_next_state = np.array(expected_next_state_list, dtype=int)

    actual_next_state = next_board_state(initial_state)

    print(f"--- Running Test: {test_name} ---")
    print("Initial State:")
    render(initial_state) # Use render to see the initial state nicely
    print("Expected Next State:")
    render(expected_next_state)
    print("Actual Next State:")
    render(actual_next_state)

    if np.array_equal(expected_next_state, actual_next_state):
        print(f"PASSED: {test_name}\n")
    else:
        print(f"FAILED: {test_name}!\n")
        print("Expected:\n", expected_next_state) # Print raw array for debugging
        print("Actual:\n", actual_next_state)     # Print raw array for debugging


if __name__ == "__main__":

    print("\n--- Verifying dead_state function ---")
    width_test_ds, height_test_ds = 5, 3
    test_dead_board = dead_state(width_test_ds, height_test_ds)

    if isinstance(test_dead_board, np.ndarray):
        print(f"PASSED: dead_state returns a NumPy array. Type: {type(test_dead_board)}")
    else:
        print(f"FAILED: dead_state does NOT return a NumPy array. Type: {type(test_dead_board)}")

    if test_dead_board.shape == (height_test_ds, width_test_ds):
        print(f"PASSED: dead_state board has correct shape {test_dead_board.shape}")
    else:
        print(f"FAILED: dead_state board has INCORRECT shape {test_dead_board.shape}. Expected: ({height_test_ds}, {width_test_ds})")

    if test_dead_board.dtype == np.int32 or test_dead_board.dtype == np.int64: # NumPy uses int32/int64 based on system architecture
        print(f"PASSED: dead_state board has correct dtype {test_dead_board.dtype}")
    else:
        print(f"FAILED: dead_state board has INCORRECT dtype {test_dead_board.dtype}. Expected: int")

    if not test_dead_board.any(): # Check if any element is non-zero (i.e., any alive cells)
        print("PASSED: dead_state board contains only zeros.")
    else:
        print("FAILED: dead_state board contains non-zero elements.")
    print("Rendered Dead Board:")
    render(test_dead_board)
    print("-" * 30 + "\n")


    print("\n--- Verifying random_state function ---")
    width_test_rs, height_test_rs = 10, 8
    test_random_board = random_state(width_test_rs, height_test_rs)

    if isinstance(test_random_board, np.ndarray):
        print(f"PASSED: random_state returns a NumPy array. Type: {type(test_random_board)}")
    else:
        print(f"FAILED: random_state does NOT return a NumPy array. Type: {type(test_random_board)}")

    if test_random_board.shape == (height_test_rs, width_test_rs):
        print(f"PASSED: random_state board has correct shape {test_random_board.shape}")
    else:
        print(f"FAILED: random_state board has INCORRECT shape {test_random_board.shape}. Expected: ({height_test_rs}, {width_test_rs})")

    if test_random_board.dtype == np.int32 or test_random_board.dtype == np.int64:
        print(f"PASSED: random_state board has correct dtype {test_random_board.dtype}")
    else:
        print(f"FAILED: random_state board has INCORRECT dtype {test_random_board.dtype}. Expected: int")

    # A simple check that it's actually random (not all zeros or all ones)
    if test_random_board.any() and not np.all(test_random_board == 1):
        print("PASSED: random_state board appears to be randomized (not all dead or all alive).")
    else:
        print("FAILED: random_state board might not be truly random (all dead or all alive).")
    print("Rendered Random Board:")
    render(test_random_board)
    print("-" * 30 + "\n")

    # --- EXISTING TESTS FOR NEXT_BOARD_STATE (modified to convert inputs to NumPy) ---

    # TEST 1: Dead cells with no live neighbors should stay dead.
    init_state_1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state_1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    run_test("Dead cells (no neighbors) stay dead", init_state_1, expected_next_state_1)

    # TEST 2: Dead cells with exactly 3 neighbors should come alive (Reproduction).
    init_state_2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state_2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    run_test("Dead cells (3 neighbors) come alive", init_state_2, expected_next_state_2)

    # TEST 3: Live cell with < 2 neighbors dies (Underpopulation).
    init_state_3 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    expected_next_state_3 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    run_test("Live cell (<2 neighbors) dies", init_state_3, expected_next_state_3)

    # TEST 4: Live cell with 2 or 3 neighbors stays alive. (Stasis)
    init_state_4_2_neighbors = [
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ]
    expected_next_state_4_2_neighbors = [
        [0,0,0], # The 1s here have only 1 neighbor each, so they die
        [1,1,1], 
        [0,0,0]
    ]
    run_test("Live cell (2 neighbors) stays alive", init_state_4_2_neighbors, expected_next_state_4_2_neighbors)

    init_state_4_3_neighbors = [
        [1,1,0],
        [0,1,0],
        [0,1,0]
    ]
    expected_next_state_4_3_neighbors = [
        [1,1,0],
        [0,1,0],
        [0,1,0]
    ]
    # This specific example is tricky because other cells also change state.
    # Let's create a simpler 3-neighbor test for clarity.

    # Simpler 3-neighbor test for a specific cell
    init_state_4_3_neighbors_simple = [
        [1,1,0],
        [1,1,0], # Testing cell (1,1) - it has 3 neighbors (0,0), (0,1), (1,0)
        [0,0,0]
    ]
    expected_next_state_4_3_neighbors_simple = [
        [1,1,0],
        [1,1,0],
        [0,0,0]
    ]
    # Here, (1,1) stays alive. Others: (0,0) has 2, stays. (0,1) has 2, stays. (1,0) has 2, stays.
    # So in this specific simple case, all 1s stay 1s.
    run_test("Live cell (3 neighbors) stays alive (simple)", init_state_4_3_neighbors_simple, expected_next_state_4_3_neighbors_simple)


    # TEST 5: Live cell with > 3 neighbors dies (Overpopulation).
    init_state_5 = [
        [1,1,1],
        [1,1,1], # Center cell has 5 neighbors
        [0,1,0]  # Center cell (1,1) has neighbors: (0,0), (0,1), (0,2), (1,0), (1,2) and (2,1) = 6 neighbors
                 # Let's adjust for exactly 4 to simplify
    ]
    # Redo init_state_5 for easier overpopulation check (center cell has 4 neighbors)
    init_state_5_overpop = [
        [0,1,0],
        [1,1,1], # Center cell (1,1)
        [0,1,0]
    ]
    # Center cell (1,1) has 4 neighbors: (0,1), (1,0), (1,2), (2,1). So it dies.
    # Other cells: (0,1) has 2. (1,0) has 2. (1,2) has 2. (2,1) has 2. All others stay alive.
    expected_next_state_5_overpop = [
        [1,1,1],
        [1,0,1], # Center cell dies and the side cells stay alive
        [1,1,1]
    ]
    run_test("Live cell (>3 neighbors) dies", init_state_5_overpop, expected_next_state_5_overpop)


    # TEST 6: Example from prompt's Hint 0
    init_state_prompt_example = [
        [1,1,0,0,1],
        [0,1,1,0,0],
        [0,1,0,0,1],
        [1,1,0,1,0],
        [1,1,1,1,1]
    ]
    expected_next_state_prompt_example = [
        [1,1,1,0,0],
        [0,0,1,1,0],
        [0,0,0,1,0],
        [0,0,0,0,0],
        [1,0,0,1,1]
    ]
    run_test("Prompt example", init_state_prompt_example, expected_next_state_prompt_example)


    # Add more tests, especially for edge cases and corners!
    # TEST 7: Corner cell (top-left) - 1 live neighbor stays dead
    init_state_corner_dead = [
        [0,1,0],
        [1,0,0],
        [0,0,0]
    ]
    expected_next_state_corner_dead = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    run_test("Corner (top-left) dead (1 neighbor) stays dead", init_state_corner_dead, expected_next_state_corner_dead)

    # TEST 8: Corner cell (top-left) - 3 live neighbors comes alive
    init_state_corner_alive = [
        [0,1,0],
        [1,1,0],
        [0,0,0]
    ]
    expected_next_state_corner_alive = [
        [1,1,0],
        [1,1,0],
        [0,0,0]
    ]
    run_test("Corner (top-left) dead (3 neighbors) comes alive", init_state_corner_alive, expected_next_state_corner_alive)
    

    print("\n" + "="*40)
    print("--- Verifying calculate_fitness function ---")
    print("="*40 + "\n")

    # TEST F1: Pattern that dies quickly (Underpopulation)
    # Expected: should survive 1 step, then die on the 2nd step. Fitness = 1.
    init_state_dies = np.array([
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ], dtype=int)
    expected_fitness_dies = 1 # Dies after 1 generation

    actual_fitness_dies = calculate_fitness(init_state_dies, num_simulation_steps=10) # Simulate for 10 steps max

    print(f"--- Running Test: Fitness - Pattern Dies Quickly ---")
    print("Initial State:")
    render(init_state_dies)
    print(f"Expected Fitness: {expected_fitness_dies}")
    print(f"Actual Fitness: {actual_fitness_dies}")
    if actual_fitness_dies == expected_fitness_dies:
        print(f"PASSED: Fitness - Pattern Dies Quickly\n")
    else:
        print(f"FAILED: Fitness - Pattern Dies Quickly! Expected {expected_fitness_dies}, Got {actual_fitness_dies}\n")


    # TEST F2: Pattern that stabilizes (Still Life - Block)
    # A block is a still life and should stabilize in the first step. Fitness = 1.
    init_state_still_life = np.array([
        [0,0,0,0],
        [0,1,1,0],
        [0,1,1,0],
        [0,0,0,0]
    ], dtype=int)
    expected_fitness_still_life = 1 # Stabilizes after 1 generation (current state == next state)

    actual_fitness_still_life = calculate_fitness(init_state_still_life, num_simulation_steps=10)

    print(f"--- Running Test: Fitness - Still Life Stabilizes ---")
    print("Initial State:")
    render(init_state_still_life)
    print(f"Expected Fitness: {expected_fitness_still_life}")
    print(f"Actual Fitness: {actual_fitness_still_life}")
    if actual_fitness_still_life == expected_fitness_still_life:
        print(f"PASSED: Fitness - Still Life Stabilizes\n")
    else:
        print(f"FAILED: Fitness - Still Life Stabilizes! Expected {expected_fitness_still_life}, Got {actual_fitness_still_life}\n")


    # TEST F3: Pattern that oscillates (Blinker - Period 2)
    # A blinker flips every generation, it should stabilize (repeat) after 2 generations. Fitness = 2.
    init_state_blinker = np.array([
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
    ], dtype=int)
    expected_fitness_blinker = 2 # Stabilizes (repeats) after 2 generations (needs period-2 check for full accuracy, otherwise might be num_simulation_steps if no period-2 check)

    # If calculate_fitness only has Period-1 check:
    expected_fitness_blinker_period1_only = 10 # Will run full steps if only Period-1 detected
    actual_fitness_blinker = calculate_fitness(init_state_blinker, num_simulation_steps=10)

    print(f"--- Running Test: Fitness - Blinker (Period 2) (Assuming Period-1 check only) ---")
    print("Initial State:")
    render(init_state_blinker)
    print(f"Expected Fitness (Period-1 check): {expected_fitness_blinker_period1_only}")
    print(f"Actual Fitness: {actual_fitness_blinker}")
    if actual_fitness_blinker == expected_fitness_blinker_period1_only:
        print(f"PASSED: Fitness - Blinker (Period 2) (Assuming Period-1 check only)\n")
    else:
        print(f"FAILED: Fitness - Blinker (Period 2) (Assuming Period-1 check only)! Expected {expected_fitness_blinker_period1_only}, Got {actual_fitness_blinker}\n")


    # TEST F4: Pattern that survives all simulation steps (e.g., a simple glider moving off board)
    # Expected: should survive num_simulation_steps.
    init_state_survives = np.array([ # A simple glider pattern
        [0,1,0,0],
        [0,0,1,0],
        [1,1,1,0],
        [0,0,0,0]
    ], dtype=int)
    expected_fitness_survives = 10 # Should run for all 10 steps

    actual_fitness_survives = calculate_fitness(init_state_survives, num_simulation_steps=10)

    print(f"--- Running Test: Fitness - Pattern Survives All Steps ---")
    print("Initial State:")
    render(init_state_survives)
    print(f"Expected Fitness: {expected_fitness_survives}")
    print(f"Actual Fitness: {actual_fitness_survives}")
    if actual_fitness_survives == expected_fitness_survives:
        print(f"PASSED: Fitness - Pattern Survives All Steps\n")
    else:
        print(f"FAILED: Fitness - Pattern Survives All Steps! Expected {expected_fitness_survives}, Got {actual_fitness_survives}\n")

    print("\n" + "="*40)
    print("--- End of Fitness Function Tests ---")
    print("="*40 + "\n")