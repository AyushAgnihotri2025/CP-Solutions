from typing import List


class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        # code here
        s = set()
        count = 0
        for i in arr:
            if i[::-1] in s:
                count += 1
            else:
                s.add(i)
        if n // 2 == count and n != 1:
            return True
        else:
            return False



#{ 
 # Driver Code Starts
class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=StringArray().Input(n)
        
        obj = Solution()
        res = obj.makePalindrome(n, arr)
        
        result_val = "YES" if res else "NO"
        print(result_val)

# } Driver Code Ends