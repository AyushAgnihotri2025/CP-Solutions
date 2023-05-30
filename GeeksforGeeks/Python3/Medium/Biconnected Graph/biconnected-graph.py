#User function Template for python3

class Solution:
    def __init__(self):
        self.time = 0

    def biGraph(self, arr, n, e):
        # code here 
        adj = [[] for i in range(n)]
        for i in range(0, 2*e, 2):
            adj[arr[i]].append(arr[i+1])
            adj[arr[i+1]].append(arr[i])
        disc = [-1 for i in range(n)]
        low = [-1 for i in range(n)]
        parent = [-1 for i in range(n)]
        ap = [False for i in range(n)]
        c = 0
        for i in range(n):
            if disc[i] == -1:
                c += 1
                self.DFS(i, disc, low, parent, ap, adj)
        if c>1 or True in ap:
            return 0
        return 1
   
    def DFS(self, u, disc, low, parent, ap, adj):
        disc[u], low[u] = self.time, self.time
        self.time += 1
        child = 0
        for v in adj[u]:
            if disc[v] == -1:
                child += 1
                parent[v] = u
                self.DFS(v, disc, low, parent, ap, adj)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and child > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v]>=disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,e=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.biGraph(arr,n,e))
# } Driver Code Ends