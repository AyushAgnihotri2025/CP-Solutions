import numpy as np
from typing import List

class Solution:
    def countSpanningTrees(self, graph : List[List[int]],m : int, n : int) -> int:
        # code here
        M = np.zeros(shape=(m, m))
        indegree = [0 for _ in range(m)]
        for edge in graph:
            u,v = edge
            M[u,v] = -1
            M[v,u] = -1
            indegree[u] += 1
            indegree[v] += 1
        for i in range(m):
            M[i,i] = indegree[i]
        noOfSpanningTrees = np.linalg.det(M[1:, 1:])
        return int(round(noOfSpanningTrees))

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
        
        a=IntArray().Input(2)
        
        
        graph=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.countSpanningTrees(graph,a[0],a[1])
        
        print(res)
        

# } Driver Code Ends