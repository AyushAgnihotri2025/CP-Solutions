# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        def collectGold(i, j, dp):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            if j == m - 1:
                return M[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            right = collectGold(i, j+1, dp)
            up = collectGold(i-1, j+1, dp) if i > 0 else 0
            down = collectGold(i+1, j+1, dp) if i < n-1 else 0
            dp[i][j] = M[i][j] + max(right, up, down)
            return dp[i][j]
        
        max_gold = 0
        dp = [[-1] * m for _ in range(n)]
        for i in range(n):
            gold = collectGold(i, 0, dp)
            max_gold = max(max_gold, gold)
        return max_gold

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends