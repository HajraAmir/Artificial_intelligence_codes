class Node:
    def __init__(self, state, parent, move, h_cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.h_cost = h_cost

    def generate_children(self):
        children = []
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in moves:
            new_state = (self.state[0] + move[0], self.state[1] + move[1])
            if 0 <= new_state[0] < 5 and 0 <= new_state[1] < 5:
                child = Node(new_state, self, move, 0)
                children.append(child)
        return children

    def calculate_heuristic(self, goal_state):
        return abs(self.state[0] - goal_state[0]) + abs(self.state[1] - goal_state[1])

class GreedyBestFirstSearch:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.open_list = []
        self.closed_list = []

    def solve(self):
        start_node = Node(self.start_state, None, None, 0)
        start_node.h_cost = start_node.calculate_heuristic(self.goal_state)
        self.open_list.append(start_node)

        while self.open_list:
            self.open_list.sort(key=lambda node: node.h_cost)
            current_node = self.open_list.pop(0)
            self.closed_list.append(current_node)

            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            children = current_node.generate_children()
            for child in children:
                child.h_cost = child.calculate_heuristic(self.goal_state)
                if child not in self.closed_list and child not in self.open_list:
                    self.open_list.append(child)
        return None

    def trace_solution(self, node):
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]

start = (0, 0)
goal = (4, 4)
solver = GreedyBestFirstSearch(start, goal)
solution = solver.solve()
print("Path:", solution)
