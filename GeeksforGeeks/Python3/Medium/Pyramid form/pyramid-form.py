#User function Template for python3

class Solution:
    def pyramidForm(self, a, N):
        # code here
        a = list(a)
        dp1 = [0]*N
        dp2 = [0]*N
        dp1[0] = min(1,a[0])
        for i in range(1,N):
            dp1[i] = min(i+1,dp1[i-1]+1,a[i])
        dp2[N-1] = min(1,a[N-1])
        for i in range(N-2,-1,-1):
            dp2[i] = min(N-i,a[i],dp2[i+1]+1)
        dp = [0]*N
        for i in range(N):
            dp[i] = min(dp1[i],dp2[i])
        mi = 0
        for i in range(N):
            if dp[i]>dp[mi]:
                mi = i
        c = 0
        h = dp[mi]
        for i in range(mi,-1,-1):
            c+=a[i]-h
            if h>0:
                h-=1
        h = dp[mi]-1
        for i in range(mi+1,N):
            c+=a[i]-h
            if h>0:
                h-=1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        a=map(int,input().split())
        
        ob = Solution()
        print(ob.pyramidForm(a,N))
# } Driver Code Ends