import numpy as np
from ga_solver import create_initial_population

TEST_POP_SIZE = 10
TEST_BOARD_WIDTH = 20
TEST_BOARD_HEIGHT = 15

print(f"--- Testing create_initial_population with pop_size={TEST_POP_SIZE}, "
    f"board_width={TEST_BOARD_WIDTH}, board_height={TEST_BOARD_HEIGHT} ---\n")

population = create_initial_population(TEST_POP_SIZE, TEST_BOARD_WIDTH, TEST_BOARD_HEIGHT)

if isinstance(population, list):
    print(f"PASSED: create_initial_population returns a Python list. Type: {type(population)}")
else:
    print(f"FAILED: create_initial_population does NOT return a Python list. Type: {type(population)}")

if len(population) == TEST_POP_SIZE:
    print(f"PASSED: Population list has the correct length ({len(population)}).")
else:
    print(f"FAILED: Population list has INCORRECT length ({len(population)}). Expected: {TEST_POP_SIZE}")

print("\n--- Verifying properties of individual boards in the population ---")
all_individuals_correct = True
for i, individual_board in enumerate(population):
    if not isinstance(individual_board, np.ndarray):
      print(f"FAILED (Individual {i}): Is NOT a NumPy array. Type: {type(individual_board)}")
      all_individuals_correct = False
      continue

    if individual_board.shape != (TEST_BOARD_HEIGHT, TEST_BOARD_WIDTH):
      print(f"FAILED (Individual {i}): Has INCORRECT shape {individual_board.shape}. Expected: ({TEST_BOARD_HEIGHT}, {TEST_BOARD_WIDTH})")
      all_individuals_correct = False

    if individual_board.dtype != np.int32 and individual_board.dtype != np.int64:
      print(f"FAILED (Individual {i}): Has INCORRECT dtype {individual_board.dtype}. Expected: int32 or int64")
      all_individuals_correct = False

    if not individual_board.any():
      print(f"WARNING (Individual {i}): Board is all zeros. May indicate an issue with random_state or low probability.")
    if np.all(individual_board == 1):
      print(f"WARNING (Individual {i}): Board is all ones. May indicate an issue with random_state or high probability.")

if all_individuals_correct:
    print("PASSED: All individual boards verified for type, shape, and dtype.")
else:
    print("FAILED: Some individual boards failed verification checks.")

print("\n--- Test Complete ---")
