#User function Template for python3

class Solution:
    def maximumPoints(self, points, n):
        # Code here
        dp=[[0]*3 for _ in range(n)]
        for i in range(3):
            dp[0][i]=points[0][i]
        for i in range(1,n):
            for j in range(3):
                if j==0:
                    dp[i][j]=max(dp[i-1][2],dp[i-1][1])+points[i][j]
                elif j==1:
                    dp[i][j]=max(dp[i-1][2],dp[i-1][0])+points[i][j]
                elif j==2:
                    dp[i][j]=max(dp[i-1][0],dp[i-1][1])+points[i][j]
        return max(dp[-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        print(ob.maximumPoints(points, n))
# } Driver Code Ends