#User function Template for python3

class Solution:
    def fillingBucket(self, n):
        # code here
        if n==1 or n==2:
            return n
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=(dp[i-1]+dp[i-2])%(10**8)
        return dp[n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.fillingBucket(N))
# } Driver Code Ends