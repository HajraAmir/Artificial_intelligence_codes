from collections import deque


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
goal_state = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 0]]  
def is_goal(state):
    return state == goal_state
def get_successors(state):
    successors = []
    blank_x, blank_y = [(x, y) for x in range(3) for y in range(3) if state[x][y] == 0][0]
    
    for dx, dy in directions:
        new_x, new_y = blank_x + dx, blank_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            successors.append(new_state)
    
    return successors


def dls(state, depth):
    if is_goal(state):
        return state, True
    if depth == 0:
        return None, False
    
    for successor in get_successors(state):
        result, found = dls(successor, depth - 1)
        if found:
            return result, True
    return None, False
def iddfs(initial_state):
    depth = 0
    while True:
        result, found = dls(initial_state, depth)
        if found:
            return result
        depth += 1
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]
solution = iddfs(initial_state)
if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found.")
