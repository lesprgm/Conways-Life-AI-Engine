# test_game_of_life.py

# To import from game_of_life.py, ensure both files are in the same directory.
# If not, you might need to adjust your PYTHONPATH or use a more advanced import structure.
# For simplicity, we'll assume they are in the same directory.
from game_of_life import next_board_state, dead_state, random_state, render, get_board_dimensions

# Helper function to run a single test case
def run_test(test_name, initial_state, expected_next_state):
    """
    Runs a single test case for next_board_state and prints the result.
    """
    actual_next_state = next_board_state(initial_state)

    print(f"--- Running Test: {test_name} ---")
    print("Initial State:")
    render(initial_state) # Use render to see the initial state nicely
    print("Expected Next State:")
    render(expected_next_state)
    print("Actual Next State:")
    render(actual_next_state)

    if expected_next_state == actual_next_state:
        print(f"PASSED: {test_name}\n")
    else:
        print(f"FAILED: {test_name}!\n")

if __name__ == "__main__":
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
        [0,1,1], # The middle 0 becomes 1
        [0,1,1], # This 1 stays 1
        [0,0,0]
    ]
    run_test("Dead cells (3 neighbors) come alive", init_state_2, expected_next_state_2)

    # TEST 3: Live cell with < 2 neighbors dies (Underpopulation).
    init_state_3 = [
        [0,0,0],
        [0,1,0], # This is the cell to test
        [0,0,0]
    ]
    expected_next_state_3 = [
        [0,0,0],
        [0,0,0], # The middle 1 should die
        [0,0,0]
    ]
    run_test("Live cell (<2 neighbors) dies", init_state_3, expected_next_state_3)

    # TEST 4: Live cell with 2 or 3 neighbors stays alive. (Stasis)
    init_state_4_2_neighbors = [
        [0,1,0],
        [0,1,0], # Cell to test
        [0,1,0]
    ]
    expected_next_state_4_2_neighbors = [
        [0,0,0], # The 1s here have only 1 neighbor each, so they die
        [0,1,0], # The center 1 has 2 neighbors and stays alive
        [0,0,0]
    ]
    run_test("Live cell (2 neighbors) stays alive", init_state_4_2_neighbors, expected_next_state_4_2_neighbors)

    init_state_4_3_neighbors = [
        [1,1,0],
        [0,1,0], # Cell to test
        [0,1,0]
    ]
    expected_next_state_4_3_neighbors = [
        [1,1,0],
        [0,1,0],
        [0,1,0]
    ]
    # For this one, the '1' at (0,0) has 1 neighbor (0,1), so it dies.
    # The '1' at (0,1) has 2 neighbors (0,0) and (1,1), so it stays.
    # The '1' at (1,1) has 3 neighbors (0,1), (0,0), (2,1), so it stays.
    # The '1' at (2,1) has 1 neighbor (1,1), so it dies.
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
        [0,1,0],
        [1,0,1], # Center cell (1,1) dies
        [0,1,0]
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
        [0,0,0,1,0], # The prompt example has a '#' here. Need to recalculate precisely.
        [0,0,0,0,0],
        [1,0,0,1,1]
    ]
    # I'll manually calculate a few for this to verify my logic,
    # or you can run this and see if it matches the *provided* expected.
    # For now, let's trust the provided expected as a reference.
    # (Manual check: cell (1,1) (initial value 1) has 4 neighbors (0,0),(0,1),(1,0),(1,2),(2,1) -> (0,0) (1), (0,1) (1), (1,0) (0), (1,2) (1), (2,0) (0), (2,1) (1), (2,2) (0)
    # The prompt's example implies (1,1) goes from 1 -> 0 (dies from overpop). It has (0,0) (1), (0,1) (1), (0,2) (0), (1,0) (0), (1,2) (1), (2,0) (0), (2,1) (1), (2,2) (0). This implies it has 4 neighbors, so it dies.
    # Cell (2,3) (initial value 0) has 3 neighbors (1,2),(1,3),(2,2),(2,4),(3,2),(3,3),(3,4) -> (1,2) (1), (1,3) (0), (2,2) (0), (2,4) (1), (3,2) (0), (3,3) (1), (3,4) (0). This implies it has 3 neighbors, so it becomes 1. This matches prompt.

    # My manual calculation for the prompt example for cell (2,3) (0-indexed)
    # init_state_prompt_example[2][3] == 0
    # Neighbors:
    # (1,2) = 1  (top-right)
    # (1,3) = 0
    # (1,4) = 0
    # (2,2) = 0  (left)
    # (2,4) = 1  (right)
    # (3,2) = 0  (bottom-left)
    # (3,3) = 1  (bottom)
    # (3,4) = 0  (bottom-right)
    # Total live neighbors = 3. So (2,3) should become 1.
    # This matches the prompt's expected output.

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