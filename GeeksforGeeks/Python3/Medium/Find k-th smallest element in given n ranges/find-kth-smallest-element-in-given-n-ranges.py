

from typing import List

class Solution:
    def kthSmallestNum(self, n : int, ranges : List[List[int]], q : int, queries : List[int]) -> List[int]:
        # code here
        ranges.sort(key=lambda x: x[0])
        stack = []
        for x, y in ranges:
            if not stack:
                stack.append((x, y))
            else:
                x0, y0 = stack[-1]
                if y0 < x:
                    stack.append((x, y))
                elif y0 < y:
                    stack[-1] = (stack[-1][0], y)
                
        values = [None]*(len(stack))
        v = 0
        for i, (s, e) in enumerate(stack):
            v += 1
            start = v
            v += (e-s)
            values[i] = (start, v)
        ans = [0]*q
        for i, qr in enumerate(queries):
            lo, hi = 0, len(values)
            while lo < hi:
                mi = lo+(hi-lo)//2
                start, end = values[mi]
                if end < qr:
                    lo = mi+1
                else:
                    hi = mi
            if lo == len(values):
                ans[i] = -1
            else:
                ans[i] = stack[lo][0] + qr-values[lo][0]
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
        
        
        ranges=IntMatrix().Input(n, 2)
        
        
        q = int(input())
        
        
        queries=IntArray().Input(q)
        
        obj = Solution()
        res = obj.kthSmallestNum(n, ranges, q, queries)
        
        IntArray().Print(res)
        

# } Driver Code Ends