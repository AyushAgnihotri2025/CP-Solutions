from typing import List


class Solution:
    def maxLevel(self, h:int,m:int) -> int:
        # code here
        def solve(h,m):
            if h<=0 or m<=0:
                return 0
            if dp[h][m]!=-1:
                return dp[h][m]
            third_sec = solve(h-2,m-8)+2
            third_first = solve(h-17,m+7)+2
            dp[h][m]=max(third_sec,third_first)
            return dp[h][m]
        dp = [[-1]*1001 for i in range(1001)]    
        return solve(h,m)-1 

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        h,m = a[0],a[1]
        obj = Solution()
        res = obj.maxLevel(h,m)
        
        print(res)
        

# } Driver Code Ends