#User function Template for python3

class Solution:
	def ShortestDistance(self, matrix):
		# Code here
        n = len(matrix)
        MAX = 10**9+7
        ans = [[0]*n for i in range(n)]

        def solve(i, j):
                if i == n-1 and j == n-1:
                    ans[i][j] = 1
                    return True
                if i >= n or j >= n or matrix[i][j] == 0:
                    return False
                jump = matrix[i][j]
                for t in range(1, jump+1):
                    if solve(i, j+t):
                        ans[i][j] = 1
                        return True
                    if solve(i+t, j):
                        ans[i][j] = 1
                        return True
                return False

        if solve(0, 0):
            return ans
        return [[-1]]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix= []
		for i in range(n):
			a = list(map(int, input().split()))
			matrix.append(a)
		ob = Solution()
		ans = ob.ShortestDistance(matrix)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends