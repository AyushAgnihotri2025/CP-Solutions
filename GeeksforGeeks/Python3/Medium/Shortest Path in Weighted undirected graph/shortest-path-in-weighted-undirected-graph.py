#User function Template for python3

from heapq import heappush, heappop
from collections import defaultdict
        
class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        heap = []
        heappush(heap,(0,1))
        dist = [float('inf')]*(n+1)
        dist[1] = 0
        parent = [i for i in range(n+1)]
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append((edge[1],edge[2]))
            adj[edge[1]].append((edge[0],edge[2]))
        while heap:
            dis, node = heappop(heap)
            for a in adj[node]:
                if dis + a[1]< dist[a[0]]:
                    dist[a[0]] = dis + a[1]
                    heappush(heap,(dis + a[1], a[0]))
                    parent[a[0]] = node
        if dist[n] == float('inf'):
            return [-1]
        path = []
        i = n
        while parent[i]!=i:
            path.append(i)
            i = parent[i]
        path.append(1)
        path.reverse()
        return path

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends