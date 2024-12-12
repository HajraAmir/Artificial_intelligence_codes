
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  
]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

def dfs(initial_state):
    visited = set()
    return dfs_recursive(initial_state, "", find_blank(initial_state), visited)

def dfs_recursive(state, path, blank_pos, visited):
    if state == goal_state:
        print("Goal state reached!")
        print_puzzle(state)
        return path
    visited.add(tuple(map(tuple, state)))

    for move, direction in zip(moves, "UDLR"):
        new_state, new_blank = make_move(state, blank_pos, move)
        if new_state and tuple(map(tuple, new_state)) not in visited:
            result = dfs_recursive(new_state, path + direction, new_blank, visited)
            if result:
                return result
    return None
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
def make_move(state, blank_pos, move):
    new_state = [row[:] for row in state]  
    x, y = blank_pos
    dx, dy = move
    new_x, new_y = x + dx, y + dy
    
    if 0 <= new_x < 3 and 0 <= new_y < 3:
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]  
        return new_state, (new_x, new_y)
    
    return None, None

def print_puzzle(state):
    for row in state:
        print(row)
    print()

initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8]
]
print("Initial State:")
print_puzzle(initial_state)

solution = dfs(initial_state)
if solution:
    print("Solution found using DFS:", solution)
else:
    print("No solution found.")
