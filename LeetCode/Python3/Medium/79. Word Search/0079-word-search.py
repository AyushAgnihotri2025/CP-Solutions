class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        p = len(board)
        q = len(board[0])
        n = len(word)

        def solve(x, y, st_ring, ind):
            if ind == n:
                return 1
            if x < 0 or x >= p or y < 0 or y >= q:
                return 0
            if board[x][y] == -1:
                return 0
            if st_ring[ind] != board[x][y]:
                return 0
            temp = board[x][y]
            board[x][y] = -1
            top_value = bot_value = left_value = right_value = 0
            bot_value = solve(x + 1, y, st_ring, ind + 1)
            right_value = solve(x, y + 1, st_ring, ind + 1)
            left_value = solve(x, y - 1, st_ring, ind + 1)
            top_value = solve(x - 1, y, st_ring, ind + 1)
            board[x][y] = temp
            return left_value or right_value or bot_value or top_value

        ind_arr = []
        for i in range(p):
            for j in range(q):
                if board[i][j] == word[0]:
                    ind_arr.append([i, j])
        for i in ind_arr:
            if solve(i[0], i[1], word, 0):
                return 1
        return 0