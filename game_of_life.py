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
    
def get_board_dimensions (board):
    height = len(board)
    if height == 0:
        return 0, 0
    width = len(board[0])
    return width, height

def next_board_state(initial_state):
    width, height = get_board_dimensions(initial_state)
    
    new_state = dead_state(width, height)
    
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    for y in range(height):
        for x in range(width):
            current_cell_value = initial_state[y][x]
            live_neighbors = 0
            
            for dy, dx in neighbor_offsets:
                neighbor_y, neighbor_x = y + dy, x + dx
                
                if 0 <= neighbor_y < height and 0 <= neighbor_x < width:
                    if initial_state[neighbor_y][neighbor_x] == 1:
                        live_neighbors += 1
                        
            if current_cell_value == 1:
                if live_neighbors < 2:
                    new_state[y][x] = 0
                elif live_neighbors == 2 or live_neighbors == 3:
                    new_state[y][x] = 1
                else:
                    new_state[y][x] = 0
            
            else:
                if live_neighbors == 3:
                    new_state[y][x] = 1
                else:
                    new_state[y][x] = 0
    return new_state
                
    
    
