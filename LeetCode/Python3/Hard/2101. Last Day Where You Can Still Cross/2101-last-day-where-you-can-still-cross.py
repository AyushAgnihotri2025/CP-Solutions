class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        _board = [[0 for _ in range(col)] for _ in range(row)]
        board = None
        
        def search(days):
            def dfs(x, y):
                res = False
                for _x, _y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if not (0 <= _x < row and 0 <= _y < col):
                        continue
                    if board[_x][_y]:
                        continue
                    if _x == row - 1:
                        return True
                    board[_x][_y] = 1
                    res |= dfs(_x, _y)
                return res
            flood(days)
            for j in range(col):
                if not board[0][j]:
                    board[0][j] = 1
                    if dfs(0, j):
                        return True
            return False
        
        def flood(days):
            nonlocal board
            board = deepcopy(_board)
            for i in range(days):
                board[cells[i][0] - 1][cells[i][1] - 1] = 1
        l, r = 0, len(cells)
        while l < r:
            mid = l + (r - l) // 2
            if search(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1