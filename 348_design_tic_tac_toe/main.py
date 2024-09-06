class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[None for _ in range(n)] for _ in range(n)]

        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diag1 = 0
        self.diag2 = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        self.update_board(row, col, player)

        return self.get_winner()
    

    def update_board(self, row, col, player):
        count_diff = 1 if player == 1 else -1
        self.rows[row] += count_diff
        self.cols[col] += count_diff

        if row == col:
            self.diag1 += count_diff
        
        if row == self.n - col - 1:
            self.diag2 += count_diff
    

    def get_winner(self):
        win_states = self.rows + self.cols + [self.diag1, self.diag2]
        for n in win_states:
            if abs(n) == self.n:
                return 1 if n > 0 else 2
        
        return 0
    
    def update_board2(self):
        self.board[row][col] = player


    def all_equal(self, arr):
        if arr[0] is None:
            return False
        
        for n in arr:
            if n != arr[0]:
                return False
        
        return True
    

    def get_winner2(self):
        # Check rows
        for row in range(self.n):
            row_values = []
            for col in range(self.n):
                row_values.append(self.board[row][col])
            if self.all_equal(row_values):
                return row_values[0]
        
        # Check cols
        for col in range(self.n):
            col_values = []
            for row in range(self.n):
                col_values.append(self.board[row][col])
            if self.all_equal(col_values):
                return col_values[0]
        
        # Check diagonals
        diag_values1 = []
        for i in range(self.n):
            diag_values1.append(self.board[i][i])
        if self.all_equal(diag_values1):
            return diag_values1[0]

        diag_values2 = []
        for i in range(self.n):
            diag_values2.append(self.board[i][-(i + 1)])
        if self.all_equal(diag_values2):
            return diag_values2[0]
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
