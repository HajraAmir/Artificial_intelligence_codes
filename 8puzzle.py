
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]


def get_blank_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def move(state, direction):
    new_state = [row[:] for row in state]  
    x, y = get_blank_pos(state)
    if direction == 'up' and x > 0:
        new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
    elif direction == 'down' and x < 2:
        new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
    elif direction == 'left' and y > 0:
        new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
    elif direction == 'right' and y < 2:
        new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
    return new_state


def is_goal(state):
    return state == GOAL_STATE

def iddfs(start, max_depth=20):
    def dls(state, depth):
        if is_goal(state):
            return []
        if depth == 0:
            return None
        for direction in ['up', 'down', 'left', 'right']:
            new_state = move(state, direction)
            result = dls(new_state, depth - 1)
            if result is not None:
                return [direction] + result
        return None

    for depth in range(max_depth):
        result = dls(start, depth)
        if result is not None:
            return result
    return None


start_state = [[1, 2, 3],
               [4, 0, 5],
               [7, 8, 6]] 

result = iddfs(start_state)
if result:
    print(f"IDDFS solution found in {len(result)} moves: {result}")
else:
    print("No solution found using IDDFS.") 
    
