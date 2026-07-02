class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if (rows.get(row) and board[row][col] in rows.get(row) or
                    cols.get(col) and board[row][col] in cols.get(col) or
                    squares.get((row // 3) * 3 + (col // 3)) and board[row][col] in squares.get((row // 3) * 3 + (col // 3))):
                    return False
                if not rows.get(row):
                    rows[row] = set()
                    rows[row].add(board[row][col])
                else:
                    rows[row].add(board[row][col])
                if not cols.get(col):
                    cols[col] = set()
                    cols[col].add(board[row][col])
                else:
                    cols[col].add(board[row][col])
                if not squares.get((row // 3) * 3 + (col // 3)):
                    squares[(row // 3) * 3 + (col // 3)] = set()
                    squares[(row // 3) * 3 + (col // 3)].add(board[row][col])
                else:
                    squares[(row // 3) * 3 + (col // 3)].add(board[row][col])
        return True
            
