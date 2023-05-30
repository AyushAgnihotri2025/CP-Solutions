#User function Template for python3

import math
class Solution:
    def subsetXOR(self, arr, N, K): 
        # code here
        m = arr[0]
        for i in range(1,N):
            if arr[i] > m:
                m = arr[i]
        M = 2**(int(math.log2(m)) + 1) - 1
        if K > M:
            return 0
        dp = [[0]*(M+1) for _ in range(N+1)]
        dp[0][0] = 1
        for i in range(1,N+1):
            for j in range(M+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j^arr[i-1]]
        return dp[N][K]

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = input().split()
        N = int(N)
        K = int(K)
        arr = input().split(' ')
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        print(ob.subsetXOR(arr,N,K))
# } Driver Code Ends