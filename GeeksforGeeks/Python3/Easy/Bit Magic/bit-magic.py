from typing import List


class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        # code here
        l = 0
        r = n - 1
        ans = 0
        
        while l <= r:
            if arr[l] != arr[r]:
                ans += 1
            l += 1
            r -= 1
        
        if ans % 2 == 0:
            return ans // 2
        else:
            return ans // 2 + 1


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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.bitMagic(n, arr)
        
        print(res)
        

# } Driver Code Ends