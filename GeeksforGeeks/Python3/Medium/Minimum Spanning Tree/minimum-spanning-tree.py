#User function Template for python3

import sys

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        sys.setrecursionlimit(10**6)
        arr = [i for i in range(V)]
        
        edges = []
        for u, nbrs in enumerate(adj):
            for v, w in nbrs:
                edges.append((u, v, w))
        edges.sort(key=lambda e: e[2])

        def find(i):
            if arr[i] != i:
                arr[i] = find(arr[i])
            return arr[i]

        ans = 0
        for (u, v, w) in edges:
            ru, rv = find(u), find(v)
            if ru != rv:
                arr[ru] = rv
                ans += w
        return ans

class DJS:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
            return self.par[u]
        return u

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        if self.rank[pu] < self.rank[pv]:
            self.par[pu] = pv
        else:
            self.par[pv] = pu
            if self.rank[pu] == self.rank[pv]:
                self.rank[pu] += 1

    def union_by_size(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            self.par[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.par[pv] = pu
            self.size[pu] += self.size[pv]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends