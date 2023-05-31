#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countPartitions(self, n, d, arr):
        # Code here
        # Calculate the target sum
        target = (sum(arr) + d) // 2
        
        # Check if target sum is achievable
        if (sum(arr) + d) % 2 != 0:
            return 0
        
        target = int(target)
        arr.sort()
        dp = [[0 for _ in range(target + 1)] for _ in range(len(arr) + 1)]
        
        # Initialize the base case
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Compute the count of partitions
        for i in range(1, n + 1):
            for j in range(target + 1):
                n_pick = dp[i - 1][j]
                pick = 0
                if j - arr[i - 1] >= 0:
                    pick = dp[i - 1][j - arr[i - 1]]
                dp[i][j] = pick + n_pick
        
        return int(dp[n][target] % (10**9 + 7))

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(n, d, arr)
        print(res)
# } Driver Code Ends