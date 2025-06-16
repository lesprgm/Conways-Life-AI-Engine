def dead_state(width, height):
    board=[]
    for i in range(height):
        row =[0]* width
        board.append(row)
    return board
    
width = 5
height = 5
initial_dead_board = dead_state(width, height)
print("Dead Board:")
for row in initial_dead_board:
    print(row)