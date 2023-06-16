#User function Template for python3

import heapq
from collections import defaultdict

class Solution:
    def exercise(self, N, M, A, src, dest, X):
        # code here
        adj = defaultdict(list)
        for node1, node2, cost in A:
            adj[node1].append((node2, cost))
            adj[node2].append((node1, cost))
        visited = set()
        heap = [(0, src)]
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if time > X:
                return "Neeman's Wool Joggers"
            if node == dest:
                return "Neeman's Cotton Classics"
            for target, cost in adj[node]:
                if not target in visited:
                    heapq.heappush(heap, (time + cost, target))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N,M,src,dest,X = map(int, input().split())
        A = [[0]*3 for i in range(M)]
        for i in range(M):
            a,b,c=map(int, input().split())
            A[i][0]=a
            A[i][1]=b
            A[i][2]=c
            
            
        ob = Solution()
        print(ob.exercise(N, M, A,src, dest,X))
# } Driver Code Ends