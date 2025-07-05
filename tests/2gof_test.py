import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_of_life import (
    dead_state,
    random_state,
    next_board_state,
    get_board_dimensions,
    render 
)

from ga_solver import (
    calculate_fitness,
    create_initial_population,
    select_parents,
    crossover,
    mutation 
)

TEST_SIMULATION_STEPS = 10

def run_test(test_name, actual, expected, comparison_func=None, render_boards=False):
    print(f"\n--- Running Test: {test_name} ---")
    passed = False
    if comparison_func:
        passed = comparison_func(actual, expected)
    elif isinstance(expected, type): 
        passed = isinstance(actual, expected)
    else:
        passed = (actual == expected)

    if render_boards:
        print("Initial State (for context):")
        if isinstance(expected, np.ndarray):
            render(expected)
        print("Actual Next State:")
        render(actual)

    if passed:
        print(f"PASSED: {test_name}")
    else:
        if isinstance(expected, type) and not isinstance(actual, expected):
             print(f"FAILED: {test_name}! Expected type {expected}, Got type {type(actual)}")
        else:
            print(f"FAILED: {test_name}! Expected {expected}, Got {actual}")

def test_dead_state():
    print("\n========================================\n--- Verifying dead_state function ---\n========================================\n")
    width, height = 5, 3
    board = dead_state(width, height)

    run_test("dead_state returns a NumPy array", type(board), np.ndarray, comparison_func=lambda a,b: isinstance(a, b))
    run_test("dead_state board has correct shape", board.shape, (height, width))
    run_test("dead_state board has correct dtype", board.dtype, np.dtype(int), comparison_func=lambda a,b: a == b)
    run_test("dead_state board contains only zeros", np.all(board == 0), True)

    print("Rendered Dead Board:")
    render(board)
    print("------------------------------\n")

def test_random_state():
    print("\n========================================\n--- Verifying random_state function ---\n========================================\n")
    width, height = 10, 8
    board = random_state(width, height)

    run_test("random_state returns a NumPy array", type(board), np.ndarray, comparison_func=lambda a,b: isinstance(a, b))
    run_test("random_state board has correct shape", board.shape, (height, width))
    run_test("random_state board has correct dtype", board.dtype, np.dtype(int), comparison_func=lambda a,b: a == b)
    
    is_randomized = not (np.all(board == 0) or np.all(board == 1))
    run_test("random_state board appears to be randomized (not all dead or all alive)", is_randomized, True)

    print("Rendered Random Board:")
    render(board)
    print("------------------------------\n")

def test_next_board_state():
    print("\n========================================\n--- Verifying next_board_state function ---\n========================================\n")

    initial_state_1 = np.zeros((3,3), dtype=int)
    expected_next_state_1 = np.zeros((3,3), dtype=int)
    actual_next_state_1 = next_board_state(initial_state_1)
    run_test("Dead cells (no neighbors) stay dead", actual_next_state_1, expected_next_state_1, comparison_func=np.array_equal, render_boards=True)

    initial_state_2 = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ], dtype=int)
    expected_next_state_2 = np.array([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ], dtype=int)
    actual_next_state_2 = next_board_state(initial_state_2)
    run_test("Dead cells (3 neighbors) come alive", actual_next_state_2, expected_next_state_2, comparison_func=np.array_equal, render_boards=True)

    initial_state_3 = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ], dtype=int)
    expected_next_state_3 = np.zeros((3,3), dtype=int)
    actual_next_state_3 = next_board_state(initial_state_3)
    run_test("Live cell (<2 neighbors) dies", actual_next_state_3, expected_next_state_3, comparison_func=np.array_equal, render_boards=True)

    initial_state_4 = np.array([
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ], dtype=int)
    expected_next_state_4 = np.array([
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ], dtype=int)
    actual_next_state_4 = next_board_state(initial_state_4)
    run_test("Live cell (2 neighbors) stays alive", actual_next_state_4, expected_next_state_4, comparison_func=np.array_equal, render_boards=True)

    initial_state_5 = np.array([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ], dtype=int)
    expected_next_state_5 = np.array([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ], dtype=int)
    actual_next_state_5 = next_board_state(initial_state_5)
    run_test("Live cell (3 neighbors) stays alive (simple)", actual_next_state_5, expected_next_state_5, comparison_func=np.array_equal, render_boards=True)

    initial_state_6 = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ], dtype=int)
    expected_next_state_6 = np.array([
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ], dtype=int)
    actual_next_state_6 = next_board_state(initial_state_6)
    run_test("Live cell (>3 neighbors) dies", actual_next_state_6, expected_next_state_6, comparison_func=np.array_equal, render_boards=True)

    initial_state_7 = np.array([
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ], dtype=int)
    expected_next_state_7 = np.array([
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ], dtype=int)
    actual_next_state_7 = next_board_state(initial_state_7)
    run_test("Glider moves one step", actual_next_state_7, expected_next_state_7, comparison_func=np.array_equal, render_boards=True)

    initial_state_8 = np.array([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ], dtype=int)
    expected_next_state_8 = np.zeros((3,3), dtype=int)
    actual_next_state_8 = next_board_state(initial_state_8)
    run_test("Corner (top-left) dead (1 neighbor) stays dead", actual_next_state_8, expected_next_state_8, comparison_func=np.array_equal, render_boards=True)

    initial_state_9 = np.array([
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ], dtype=int)
    expected_next_state_9 = np.array([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ], dtype=int)
    actual_next_state_9 = next_board_state(initial_state_9)
    run_test("Corner (top-left) dead (3 neighbors) comes alive", actual_next_state_9, expected_next_state_9, comparison_func=np.array_equal, render_boards=True)

    print("\n========================================\n--- End of next_board_state tests ---\n========================================\n")

def test_calculate_fitness():
    print("\n========================================\n--- Verifying calculate_fitness function ---\n========================================\n")

    initial_state_1 = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ], dtype=int)
    expected_fitness_1 = 1
    actual_fitness_1 = calculate_fitness(initial_state_1, TEST_SIMULATION_STEPS)
    run_test("Fitness - Pattern Dies Quickly", actual_fitness_1, expected_fitness_1)

    initial_state_2 = np.array([
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ], dtype=int)
    expected_fitness_2 = 2
    actual_fitness_2 = calculate_fitness(initial_state_2, TEST_SIMULATION_STEPS)
    run_test("Fitness - Still Life Stabilizes", actual_fitness_2, expected_fitness_2)

    initial_state_3 = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ], dtype=int)
    expected_fitness_3 = 2
    actual_fitness_3 = calculate_fitness(initial_state_3, TEST_SIMULATION_STEPS)
    run_test("Fitness - Blinker (Period 2)", actual_fitness_3, expected_fitness_3)

    initial_state_4 = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ], dtype=int)
    expected_fitness_4 = TEST_SIMULATION_STEPS
    actual_fitness_4 = calculate_fitness(initial_state_4, TEST_SIMULATION_STEPS)
    run_test("Fitness - Pattern Survives All Steps (Glider)", actual_fitness_4, expected_fitness_4)

    print("\n========================================\n--- End of calculate_fitness tests ---\n========================================\n")

if __name__ == "__main__":
    test_dead_state()
    test_random_state()
    test_next_board_state()
    test_calculate_fitness()

    print("\n\nAll tests completed.")
