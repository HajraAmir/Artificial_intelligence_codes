import heapq

def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def manhattan_distance(state, goal_state):
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0: 
                goal_pos = [(row, col) for row in range(3) for col in range(3) if goal_state[row][col] == state[i][j]][0]
                dist += abs(goal_pos[0] - i) + abs(goal_pos[1] - j)
    return dist

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost  
        self.h_cost = h_cost 
        self.f_cost = g_cost + h_cost 
    def generate_children(self, goal_state):
        children = []
        empty_row, empty_col = find_empty_tile(self.state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        for move in moves:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in self.state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                h_cost = manhattan_distance(new_state, goal_state)
                child_node = PuzzleNode(new_state, self, move, self.g_cost + 1, h_cost)
                children.append(child_node)
        
        return children

    def __lt__(self, other):
        return self.f_cost < other.f_cost


class AStarSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.open_list = []  
        self.closed_list = set()  
    def solve(self):
        start_node = PuzzleNode(self.start_state, g_cost=0, h_cost=manhattan_distance(self.start_state, self.goal_state))
        heapq.heappush(self.open_list, start_node)

        while self.open_list:
            current_node = heapq.heappop(self.open_list)
            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            self.closed_list.add(self.tupled_state(current_node.state))
            for child in current_node.generate_children(self.goal_state):
                if self.tupled_state(child.state) not in self.closed_list:
                    heapq.heappush(self.open_list, child)

        return None
    def tupled_state(self, state):
        return tuple(tuple(row) for row in state)
    def trace_solution(self, node):
        solution_path = []
        while node.parent is not None:
            solution_path.append(node.state)
            node = node.parent
        solution_path.reverse()
        return solution_path


    def is_solvable(self, state):
        llist = sum(state, [])
        inversions = sum(1 for i in range(len(llist)) for j in range(i + 1, len(llist)) if llist[i] > llist[j] and llist[i] != 0 and llist[j] != 0)
        return inversions % 2 == 0
def print_state(state):
    for row in state:
        print(row)
    print()


if __name__ == "__main__":
    start_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solver = AStarSolver(start_state, goal_state)

    if solver.is_solvable(start_state):
        solution = solver.solve()
        if solution:
            for step in solution:
                print_state(step)
        else:
            print("No solution found.")
    else:
        print("The puzzle is unsolvable.")
