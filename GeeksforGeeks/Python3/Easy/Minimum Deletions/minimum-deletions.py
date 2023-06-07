#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here
        n=len(S)
        dp=[[0 for i in range(n+1)]for i in range(n+1)]
        for i in range(n):
            dp[i+1][i+1]=1
        for i in range(n-1):
            # print("hello")
            if(S[i]==S[i+1]):
                dp[i+1][i+2] = 2
            else:
                dp[i+1][i+2] = 1
        # print(dp[1])
        # print(dp[2])
        for l in range(3,n+1):
            for i in range(0,n+1-l):
                x=i+1
                y=i+l
                if(S[x-1]!=S[y-1]):
                    dp[x][y]=max(dp[x][y-1],dp[x+1][y])
                else:
                    dp[x][y]=2+dp[x+1][y-1]
        return n-dp[1][n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends