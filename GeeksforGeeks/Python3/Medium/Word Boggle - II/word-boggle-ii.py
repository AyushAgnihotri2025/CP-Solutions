#User function Template for python3

class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        n = len(dictionary)
        rows = len(board)
        cols = len(board[0])
        self.ans = []
        visited = [[False]*cols for _ in range(rows)]

        def dfs(r, c, word, index, visited):
            if word[index] != board[r][c]:
                return False
            if index == len(word)-1:
                return True
            visited[r][c] = True
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in direction:
                new_r = r + dr
                new_c = c + dc
                if new_r in range(rows) and new_c in range(cols) and not visited[new_r][new_c]:
                    if dfs(new_r, new_c, word, index+1, visited):
                        visited[r][c] = False
                        return True
            visited[r][c] = False
            return False

        def exists(word, board):
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == word[0]:
                        if dfs(r, c, word, 0, visited):
                            return True
            return False

        dictionary = list(set(dictionary))
        for word in dictionary:
            if exists(word, board):
                self.ans.append(word)
        return self.ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()                               # sorting output
        for i in found:
            print(i,end=' ')
        print()
# } Driver Code Ends