class AlphaBetaPruning:
    def __init__(self, game_state, player):
        self.game_state = game_state  
        self.player = player  
        self.nodes_evaluated = 0  

    def is_terminal(self, state):
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] and state[i][0] != '_':
                return True, state[i][0]  
            if state[0][i] == state[1][i] == state[2][i] and state[0][i] != '_':
                return True, state[0][i]  

        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != '_':
            return True, state[0][0]
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != '_':
            return True, state[0][2]

        for row in state:
            if '_' in row:
                return False, None  

        return True, 'draw'  

    def utility(self, state):
        terminal, winner = self.is_terminal(state)
        if terminal:
            if winner == 'X':
                return 1 
            elif winner == 'O':
                return -1
            else:  
                return 0
        return None 

    def alphabeta(self, state, depth, alpha, beta, maximizing_player):
        score = self.utility(state)
        if score is not None:
            self.nodes_evaluated += 1  
            return score

        if maximizing_player:
            max_eval = -float('inf')  
            for i in range(3):
                for j in range(3):
                    if state[i][j] == '_':  
                        state[i][j] = 'X'  
                        eval = self.alphabeta(state, depth - 1, alpha, beta, False)
                        state[i][j] = '_'
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:  
                            break
            return max_eval
        else:
            min_eval = float('inf')  
            for i in range(3):
                for j in range(3):
                    if state[i][j] == '_':  
                        state[i][j] = 'O'  
                        eval = self.alphabeta(state, depth - 1, alpha, beta, True)
                        state[i][j] = '_'
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def best_move(self):
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.game_state[i][j] == '_':  
                    self.game_state[i][j] = 'X'  
                    score = self.alphabeta(self.game_state, 0, -float('inf'), float('inf'), False)
                    self.game_state[i][j] = '_'
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

if __name__== "__main__":
    board = [
        ['X', 'O', 'X'],
        ['O', 'X', '_'],
        ['_', '_', 'O']  
    ]
    alphabeta = AlphaBetaPruning(board, 'X')
    move = alphabeta.best_move()

    print(f"Best move for 'X' (Alpha-Beta Pruning): {move}")
    print(f"Nodes evaluated (Alpha-Beta Pruning): {alphabeta.nodes_evaluated}")
