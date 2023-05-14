from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, A : List[int]) -> int:
        # code here
        take=n_take=0
        for i in A:
            take,n_take=max(i+take,n_take),i+take
        return max(take,n_take)



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
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.findMaxSubsetSum(N, A)
        
        print(res)
        

# } Driver Code Ends