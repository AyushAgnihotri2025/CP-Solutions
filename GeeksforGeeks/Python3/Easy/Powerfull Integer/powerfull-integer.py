from typing import List

class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        # code here
        ints = []
        for start, end in intervals:
            ints.extend([(start, -1), (end, 1)])
        ints.sort()
        
        n, ans = 0, -1
        for time, typ in ints:
            if typ == -1:
                n += 1
            else:
                if n >= k:
                    ans = max(ans, time)
                n -= 1
        return ans

#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        intervals=IntMatrix().Input(n, 2)
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.powerfullInteger(n, intervals, k)
        
        print(res)
        

# } Driver Code Ends