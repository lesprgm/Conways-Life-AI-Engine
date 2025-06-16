import random

def dead_state(width, height):
    board=[]
    for i in range(height):
        row =[0]* width
        board.append(row)
    return board

def random_state(width,height):
    cell_state = dead_state(width,height)
    for x in range(height):
        for y in range(width):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state[y][x] = 1
            else:
                cell_state[y][x] = 0
    return cell_state
    
width = 5
height = 5
initial_dead_board = random_state(width, height)
print("Random Board:")
for row in initial_dead_board:
    print(row)