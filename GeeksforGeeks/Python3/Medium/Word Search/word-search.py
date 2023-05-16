from itertools import product
from collections import Counter
class Solution:
	def isWordExist(self, board, word):
		#Code here
		m, n = len(board), len(board[0])
		b = Counter(board[i][j] for i, j in product(range(m), range(n)))
		w = Counter(word)
		if len(w) > len(b): 
		    return 0
		def dfs(r, c, index):
		    if index == len(word): 
		        return 1
		    if r < 0 or r == m or c < 0 or c == n or board[r][c] != word[index]: return 0
		    board[r][c] = '@'
		    if dfs(r + 1, c, index + 1): 
		        return 1
		    if dfs(r - 1, c, index + 1): 
		        return 1
		    if dfs(r, c + 1, index + 1): 
		        return 1
		    if dfs(r, c - 1, index + 1): 
		        return 1
		    board[r][c] = word[index]
		for i, j in product(range(m), range(n)):
		    if dfs(i, j, 0): 
		        return 1
		   
		return 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n, m = map(int, input().split())
		board = []
		for i in range(n):
			a = list(input().strip().split())
			b = []
			for j in range(m):
				b.append(a[j][0])
			board.append(b)
		word = input().strip()
		obj = Solution()
		ans = obj.isWordExist(board, word)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends