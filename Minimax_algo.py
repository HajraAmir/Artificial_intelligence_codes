class Minimax:
    def __init__(self, board):
        self.board = board
        self.nodes_evaluated = 0  

    def is_terminal(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
                return True, board[i][0]  
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
                return True, board[0][i]  

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
            return True, board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
            return True, board[0][2]

        for row in board:
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

    def minimax(self, board, is_maximizer):
        score = self.utility(board)
        if score is not None:
            self.nodes_evaluated += 1  
            return score

        if is_maximizer:
            best_score = -float('inf')  
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':  
                        board[i][j] = 'X'  
                        score = self.minimax(board, False)
                        board[i][j] = '_'
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_': 
                        board[i][j] = 'O'  
                        score = self.minimax(board, True)
                        board[i][j] = '_'  
                        best_score = min(best_score, score)
            return best_score

    def best_move(self):
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':  
                    self.board[i][j] = 'X' 
                    score = self.minimax(self.board, False)
                    self.board[i][j] = '_'  
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
    minimax = Minimax(board)
    move = minimax.best_move()

    print(f"Best move for 'X' (Minimax): {move}")
    print(f"Nodes evaluated (Minimax): {minimax.nodes_evaluated}")
