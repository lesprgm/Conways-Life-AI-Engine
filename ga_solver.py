import numpy as np
import main
from game_of_life import(next_board_state)

def calculate_fitness ( board, num_simulation_steps):
    current_sim_board = board.copy()
    previous_sim_board = None
    step_count = 0
    for step_count in range(num_simulation_steps):
        next_sim_board = next_board_state(current_sim_board)
        step_count += 1
        
        if not next_sim_board.any():
            return step_count
        if previous_sim_board is not None and np.array_equal(next_sim_board, previous_sim_board):
            return step_count
        return num_simulation_steps