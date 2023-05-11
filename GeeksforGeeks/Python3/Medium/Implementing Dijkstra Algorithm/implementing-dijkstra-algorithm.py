import heapq
from collections import deque
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist=[float("inf") for i in range(V)]
        dist[S] = 0
        q=deque([])
        q.append(S)
        while q:
            a = q.popleft()
            for i in adj[a]:
                f,g=i[0],i[1]
                if dist[f]>dist[a]+g:
                    dist[f]=dist[a]+g
                    q.append(f)
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends