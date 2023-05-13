#User function Template for python3

class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,N):
        # code here
        dp = [0]*(N+1)
        dp[0]=1
        dp[1]=1
        MOD = 10**9 + 7
        
        for i in range(2,N+1):
            
            count = 0
            
            for j in range(1,i+1):
                
                leftBST = dp[j-1]
                rightBST = dp[i-j]
                count += ((leftBST*rightBST))
            dp[i]=count%MOD
        return dp[-1]    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n = int(input());
        ob=Solution()
        print(ob.numTrees(n))
# } Driver Code Ends