from typing import List

class Solution:
    def kthLargest(self, N : int, K : int, Arr : List[int]) -> int:
        # code here
        ans=[]
        for i in range(0,N):
            sum=0
            for j in range(i,N):
                sum+=Arr[j]
                ans.append(sum)
        ans.sort(reverse=True)
        return ans[K-1]

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
        
        
        Arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.kthLargest(N, K, Arr)
        
        print(res)
        

# } Driver Code Ends