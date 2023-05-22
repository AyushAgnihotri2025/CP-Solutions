from typing import List


class Solution:
    def solve(self, N : int, p : List[int]) -> int:
        # code here
        count=0
        dict={}
        for i in p:
            if i== (-1) or i ==0:
                continue
            else:
                if i not in dict:
                    dict[i]=1
                    count+=1
                dict[i]+=1
        return count

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
        
        
        p=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, p)
        
        print(res)
        

# } Driver Code Ends