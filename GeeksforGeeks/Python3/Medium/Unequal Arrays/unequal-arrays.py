from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        A.sort()
        B.sort()
        evens_A, odds_A = [], []
        evens_B, odds_B = [], []
        sum_A, sum_B = sum(A), sum(B)
        for ele_A, ele_B in zip(A, B):
            if ele_A & 1:
                odds_A.append(ele_A)
            else:
                evens_A.append(ele_A)
            
            if ele_B & 1:
                odds_B.append(ele_B)
            else:
                evens_B.append(ele_B)
        if sum_A != sum_B or len(evens_A) != len(evens_B):
            return -1
        ops = 0
        for ea, eb in zip(evens_A, evens_B):
            ops += abs(ea - eb) >> 1
        for oa, ob in zip(odds_A, odds_B):
            ops += abs(oa - ob) >> 1
        return ops >> 1
        



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
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, A, B)
        
        print(res)
        

# } Driver Code Ends