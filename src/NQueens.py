class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, n):
        board = [["."] * n for _ in range(n)]
        def checkBoard(row, col,board):
            # Check current row and col
            for prev_col in range(col):
                if board[row][prev_col] == 'Q':
                    return False
            for prev_row in range(row):
                if board[prev_row][col] == 'Q':
                    return False
            diag_row, diag_col = row, col
            while diag_row >= 0 and diag_col >= 0:
                if board[diag_row][diag_col] == 'Q':
                    return False
                diag_row -= 1
                diag_col -= 1
            diag_row, diag_col = row, col
            while diag_row >= 0 and diag_col < n:
                if board[diag_row][diag_col] == 'Q':
                    return False
                diag_row -= 1
                diag_col += 1
            return True
            
        def solve(board,qn,ans):
            if qn==n:
                to_append = [''.join(sa) for sa in board]
                ans.append(to_append)
                return
        
            for c in range(n):
                if checkBoard(qn,c,board):
                    board[qn][c] = 'Q'
                    solve(board,qn+1,ans)
                    board[qn][c] = '.'
        
        ans = list()
        solve(board,0,ans)
        return ans

