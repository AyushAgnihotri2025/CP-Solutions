class Solution:

    #Function to detect cycle using DSU in an undirected graph.
	def detectCycle(self, V, adj):
		# Code here
		self.Parent = dict()
        self.rank = dict()
        self.count = 0
        edges = set()
        for u in range(V):
            for v in adj[u]:
                if ((u,v) not in edges) and ((v,u) not in edges):
                    edges.add((u,v))
        for u,v in edges:
            if self.connect(u, v):
                return 1
        return 0
    
    def add(self, v):
        if v not in self.Parent:
            self.Parent[v] = v
            self.rank[v] = self.count
            self.count += 1 
    
    def getParent(self, v):
        if v in self.Parent:
            if self.Parent[v] != v:
                self.Parent[v] = self.getParent(self.Parent[v])
        else:
            self.add(v)
        return self.Parent[v]
    
    def connect(self, u, v):
        pu =  self.getParent(u)
        pv = self.getParent(v)
        if pu == pv:
            return True
        else:
            if self.rank[pu] < self.rank[pv]:
                self.Parent[pv] = pu
            elif self.rank[pu] > self.rank[pv]:
                self.Parent[pu] = pv
            else:
                self.Parent[pv] = pu
                self.rank[pv] += 1
            return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.detectCycle(V, adj)
		print(ans)
# } Driver Code Ends