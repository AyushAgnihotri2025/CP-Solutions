#User function Template for python3

class Solution:
    def solve(self, arr, i, dp):
        if arr[i] == -1:
            return 1
        if dp[i] != -1:
            return dp[i]
        return self.solve(arr, arr[i], dp) + 1
        
    def findHeight(self, N, arr):
        # code here
        dp = [-1] * N
        ans = 0
        for i in range(N):
            ans = max(ans, self.solve(arr, i, dp))
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.findHeight(N, arr))
# } Driver Code Ends