class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        return self.check_in_row() and self.check_in_col() and self.check_in_box()

    def check_in_row(self):
        for i in range(9):
            record = [0 for m in range(10)]
            for j in range(9):
                if self.board[i][j] != ".":
                    if record[int(self.board[i][j])] != 0:
                        return False
                    record[int(self.board[i][j])] = 1
        return True

    def check_in_col(self):
        for i in range(9):
            record = [0 for m in range(10)]
            for j in range(9):
                if self.board[j][i] != ".":
                    if record[int(self.board[j][i])] != 0:
                        return False
                    record[int(self.board[j][i])] = 1
        return True

    def check_in_box(self):
        for i in range(0, 9, 3):
            for j in range(0, 9 ,3):
                record = [0 for c in range(10)]
                for m in range(0, 3):
                    for n in range(0, 3):
                        if self.board[i+m][j+n] != ".":
                            if record[int(self.board[i+m][j+n])] != 0:
                                return False
                            record[int(self.board[i+m][j+n])] = 1
        return True