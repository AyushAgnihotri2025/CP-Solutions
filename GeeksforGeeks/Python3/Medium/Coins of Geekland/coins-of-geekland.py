#User function Template for python3

class Solution:
    def Maximum_Sum(self, mat, N, K):
        # Your code goes here
        prefix=[[0]*(N+1) for _ in range(N+1)]
        for i in range(N):
            for j in range(N):
                prefix[i+1][j+1]=prefix[i+1][j]+prefix[i][j+1]-prefix[i][j]+mat[i][j]
        maxSum=float('-inf')
        for i in range(K,N+1):
            for j in range(K,N+1):
                currSum=prefix[i][j] - prefix[i-K][j] - prefix[i][j-K] + prefix[i-K][j-K]
                maxSum=max(maxSum,currSum)
        return maxSum

#{ 
 # Driver Code Starts


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        matrix=[]
        for _ in range(n):
            matrix.append( [ int(x) for x in input().strip().split() ] )
        k=int(input())
        obj = Solution()
        print(obj.Maximum_Sum(matrix,n,k))
# } Driver Code Ends