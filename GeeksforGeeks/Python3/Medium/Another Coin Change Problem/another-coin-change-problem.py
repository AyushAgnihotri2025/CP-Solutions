from typing import List


class Solution:
    def makeChanges(self, N : int, K : int, target : int, coins : List[int]) -> bool:
        # code here
        coins.sort()
        prev, cur = set(coins), set()
        for times in range(1, K):
            cur.clear()
            for v in prev:
                for c in coins:
                    if v + c > target: break
                    cur.add(v+c)
            prev, cur = cur, prev
        return target in prev

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
        
        N = int(input())
        
        
        K = int(input())
        
        
        target = int(input())
        
        
        coins=IntArray().Input(N)
        
        obj = Solution()
        res = obj.makeChanges(N, K, target, coins)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends