#User function Template for python3
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, arr, N, target):
        # code here 
        dp1, dp2 = defaultdict(int), defaultdict(int) 
        dp1[0] = 1
        for av in arr:            
            for dv, cnt in dp1.items(): 
                dp2[dv+av] += cnt
                dp2[dv-av] += cnt
            dp1, dp2 = dp2, dp1
            dp2.clear()
        return dp1.get(target, 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(arr,N, target))
# } Driver Code Ends