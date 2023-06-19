#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        # Code here
        dp=[[False for x in range(K+1)] for x in range(N+1)]
        dp[N][0]=True
        for index in range(N-1,-1,-1):
            for target in range(K+1):
                t1=False
                t2=False
                if arr[index]<=target:
                    if dp[index+1][target-arr[index]]:
                        t1=True
                if dp[index+1][target]:
                    t2=True
                if t1 or t2:
                    dp[index][target]=True
                else:
                    dp[index][target]=False
        return dp[0][K]
    def function(self, arr, index, target, n, dp):
        if index==n:
            if target==0:
                return True
            else:
                return False
        if dp[index][target]!=-1:
            return dp[index][target]
        if arr[index]<=target:
            if self.function(arr, index+1, target-arr[index], n, dp):
                dp[index][target]=True
                return True
        if self.function(arr, index+1, target, n, dp):
            dp[index][target]=True
            return True
        dp[index][target]=False
        return False

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        K = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        possible = ob.checkSubsequenceSum(N, arr, K)
        print('Yes' if possible else 'No')
# } Driver Code Ends