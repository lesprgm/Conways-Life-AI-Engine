import random

def dead_state(width, height):
    board=[]
    for i in range(height):
        row =[0]* width
        board.append(row)
    return board

def random_state(width,height):
    cell_state = dead_state(width,height)
    for y in range(height):
        for x in range(width):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state[y][x] = 1
            else:
                cell_state[y][x] = 0
    return cell_state

def render(board_state):
    height = len(board_state)
    width = len(board_state[0])
    print("-" * (width + 2))
    
    for y in range(height):
        row_string = "|"
        for x in range(width):
            cell = board_state[y][x]
            if cell == 1:
                row_string += "#"
            else:
                row_string += " "
        row_string += "|"
        print(row_string)
        
    print("-" * (width + 2))

    
