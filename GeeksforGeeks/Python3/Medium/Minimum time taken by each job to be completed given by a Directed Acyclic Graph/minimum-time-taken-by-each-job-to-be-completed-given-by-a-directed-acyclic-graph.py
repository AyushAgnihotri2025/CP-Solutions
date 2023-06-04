from sys import maxsize
from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        job = [maxsize] * (n+1)
        adj = defaultdict(list)
        indeg = defaultdict(int)
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1
        q = deque()
        for i in range(1, n+1):
            if indeg[i] == 0:
                q.append(i)
                job[i] = 1
        while q:
            node = q.popleft()
            for nbr in adj[node]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    job[nbr] = 1 + job[node]
                    q.append(nbr)
        return ' '.join([str(x) for x in job[1:]])

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
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends