#User function Template for python3

 #Your task is to complete this Function \

class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        n = len(A)
        m = len(B)
        if n + m != len(C):
            return False
    
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[n][m] = 1
        for i in range(n - 1, -1, -1):
            if C[i + m] == A[i]:
                dp[i][m] = dp[i + 1][m]
        for j in range(m - 1, -1, -1):
            if C[n + j] == B[j]:
                dp[n][j] = dp[n][j + 1]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if A[i] == C[i + j] and B[j] != C[i + j]:
                    dp[i][j] = dp[i + 1][j]
                elif B[j] == C[i + j] and A[i] != C[i + j]:
                    dp[i][j] = dp[i][j + 1]
                elif A[i] == C[i + j] and B[j] == C[i + j]:
                    dp[i][j] = dp[i + 1][j] | dp[i][j + 1]
        return dp[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if Solution().isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)
# contributed By: Harshit Sidhwa
# } Driver Code Ends