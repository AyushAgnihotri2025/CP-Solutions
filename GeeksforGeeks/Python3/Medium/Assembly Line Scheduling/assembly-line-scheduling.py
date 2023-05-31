from typing import List

class Solution:
    def carAssembly(self, n : int, a : List[List[int]], T : List[List[int]], e : List[int], x : List[int]) -> int:
        # code here
        line0 = e[0] + a[0][0]
        line1 = e[1] + a[1][0]
        for i in range(1, len(a[0])):
            curLine0 = a[0][i] + min(line0, line1 + T[1][i])
            curLine1 = a[1][i] + min(line1, line0 + T[0][i])
            line0 = curLine0
            line1 = curLine1
        return min(line0 + x[0], line1 + x[1])

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
        
        
        a=IntMatrix().Input(2, 2)
        
        
        T=IntMatrix().Input(2, 2)
        
        
        e=IntArray().Input(2)
        
        
        x=IntArray().Input(2)
        
        obj = Solution()
        res = obj.carAssembly(n, a, T, e, x)
        
        print(res)
        

# } Driver Code Ends