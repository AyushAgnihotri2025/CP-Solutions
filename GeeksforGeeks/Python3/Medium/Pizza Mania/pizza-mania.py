#User function Template for python3

class Solution:
    def rec(self, i, x, s, m, l, cs, cm, cl, dp):
        if i>=x:
            return 0
        elif dp[i]!=-1:
            return dp[i]
        a = self.rec(i+s, x, s, m, l, cs, cm, cl, dp)+cs
        b = self.rec(i+m, x, s, m, l, cs, cm, cl, dp)+cm
        c = self.rec(i+l, x, s, m, l, cs, cm, cl, dp)+cl
        dp[i] = min(a,b,c)
        return dp[i]

    def getPizza(self, X, S, M, L, CS, CM, CL):
        # code here
        dp = [-1]*(2*X)
        return self.rec(0,X,S,M,L,CS,CM,CL,dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X,S,M,L,CS,CM,CL=map(int,input().split())
        
        ob = Solution()
        print(ob.getPizza(X,S,M,L,CS,CM,CL))
# } Driver Code Ends