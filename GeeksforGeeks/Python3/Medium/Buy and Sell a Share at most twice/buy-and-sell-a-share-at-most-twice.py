from typing import List

class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 0:
                        dp[ind][buy][cap] = max(0 + dp[ind+1][0][cap], - price[ind] + dp[ind+1][1][cap])
                    if buy == 1:
                        dp[ind][buy][cap] = max(0 + dp[ind+1][1][cap], price[ind] + dp[ind+1][0][cap-1])
        return dp[0][0][2]

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
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends