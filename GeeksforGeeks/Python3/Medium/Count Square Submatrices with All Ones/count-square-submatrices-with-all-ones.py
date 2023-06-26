#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countSquares(self, N, M, matrix):
        # Code here
        dp = [[0 for i in range(M)] for j in range(N)]
        maxi = 0
        for i in range(1, N):
            dp[i][0] = matrix[i][0]
            maxi+=matrix[i][0]
        for j in range(M):
            dp[0][j] = matrix[0][j]
            maxi+=matrix[0][j]
        for i in range(1, N):
            for j in range(1, M):
                if matrix[i][j]==1:
                    dp[i][j]=1
                    dp[i][j]+=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    maxi += dp[i][j]
        return maxi


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, M = list(map(int, input().split()))
        matrix = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.countSquares(N, M, matrix)
        print(res)
# } Driver Code Ends