#User function Template for python3

class Solution:
    def f(self,i,j,s1,s2,dp):
        if j==0:
            return 1
        if i==0:
            return 0
        if dp[i][j]==-1:
            if s1[i-1]==s2[j-1]:
                dp[i][j]=self.f(i-1,j-1,s1,s2,dp)+self.f(i-1,j,s1,s2,dp)
            else:
                dp[i][j]=self.f(i-1,j,s1,s2,dp)
        return dp[i][j]
     
    def countWays(self, S1, S2):
        # code here
        n=len(S1)
        m=len(S2)
        dp=[[-1 for i in range(m+1)]for j in range(n+1)]
        return self.f(n,m,S1,S2,dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        S1 = input()
        S2 = input()
        ob = Solution()
        ans = ob.countWays(S1,S2)
        print(ans)
# } Driver Code Ends