#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minimizeSum(self, n, triangle):
        # Code here
        ans=[0 for j in range(n)]
        for j in range(n):
            ans[j]=triangle[n-1][j]
        for i in range(n-2 ,-1,-1):
            curr=[0 for i in range(n)]
            for j in range(i,-1,-1):
                curr[j]=triangle[i][j]+min(ans[j],ans[j+1])
            ans=curr
        return ans[0]


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        triangle = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.minimizeSum(n, triangle)
        print(res)
# } Driver Code Ends