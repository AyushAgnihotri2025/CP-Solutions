class Solution:
    def maxCoins(self,arr, n):
        # Code here
        dp=[[-1]*n for _ in range(n)]
        if n==1:
            return arr[0]

        def helper(i,j,sum1):
            if i+1==j:
                return max(arr[i],arr[j])
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=max(sum1-helper(i+1,j,sum1-arr[i]),sum1-helper(i,j-1,sum1-arr[j]))
            return dp[i][j]

        return helper(0,n-1,sum(arr))

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends