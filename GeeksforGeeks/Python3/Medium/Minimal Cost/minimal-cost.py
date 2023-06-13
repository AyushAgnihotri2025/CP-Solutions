#User function Template for python3

class Solution:
    def minimizeCost(self, height, n, k):
        dp=[0 for _ in range(n)]
        dp[0]=0
        for i in range(1,n):
            dp[i]=min([dp[i-j]+abs(height[i]-height[i-j]) if 0<=i-j else float("inf") for j in range(1,k+1)])
        return dp[n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimizeCost(height, n, k))
# } Driver Code Ends