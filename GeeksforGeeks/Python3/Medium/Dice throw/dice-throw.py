#User function Template for python3

def solve(dice,face,target):
    # Base Cases
    if (target < 0):
        return 0
    if(target != 0 and dice == 0):
        return 0
    if (dice != 0 and target == 0):
        return 0
    if (dice ==0 and target == 0):
        return 1
    ans = 0
    for i in range(1,face+1):
        ans = ans + solve(dice-1, face, target - i)
    return ans
    
def solveMem(dice,face,target,dp):
    # Base Cases
    if (target < 0):
        return 0
    if(target != 0 and dice == 0):
        return 0
    if (dice != 0 and target == 0):
        return 0
    if (dice ==0 and target == 0):
        return 1
    if dp[dice][target] != -1:
        return dp[dice][target]
    ans = 0
    for i in range(1,face+1):
        ans = ans + solveMem(dice-1, face, target - i,dp)
    dp[dice][target] = ans
    return dp[dice][target]

def solveTab(d,face,t):
    prev = [0]*(t+1)
    curr = [0]*(t+1)
    prev[0] = 1
    
    for dice in range(1,d+1):
        for target in range(1,t+1):
            ans = 0
            for i in range(1,face+1):
                if target-i >= 0:
                    ans = ans + prev[target - i]
            curr[target] = ans
        prev = curr
        curr = [0]*(t+1)
    return prev[t]
    
class Solution:
    def noOfWays(self, M, N, X):
        # code here
        return solveTab(N,M,X)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        M,N,X=map(int,input().split())
        
        ob = Solution()
        print(ob.noOfWays(M,N,X))
# } Driver Code Ends