# Your task is to complete this function
# Finction should return Integer
class Solution:
    def sequenceCount(self,arr1, arr2):
        # Code here
        n=len(arr1)
        m=len(arr2)

        if n<m:
            return 0

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=1

        for i in range(1,n+1):
            for j in range(1,m+1):
                p1=dp[i-1][j]
                p2=0
                if arr1[i-1]==arr2[j-1]:
                    p2=dp[i-1][j-1]
                dp[i][j]=(p1+p2)%1000000007
        return dp[n][m]

#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends