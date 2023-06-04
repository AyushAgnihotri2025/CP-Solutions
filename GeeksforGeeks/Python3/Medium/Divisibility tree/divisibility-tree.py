#User function Template for python3

class Solution:
    def dfs(self, adj, v, p):
        if v != 0 and len(adj[v]) == 1:
            return 1
        ans = 1
        for w in adj[v]:
            if w == p:
                continue
            cnt = self.dfs(adj, w, v)
            if cnt % 2 == 0:
                self.ans += 1
            ans += cnt
        return ans
        
    def minimumEdgeRemove(self, n, edges):
        #Code here
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]-1].append(e[1]-1)
            adj[e[1]-1].append(e[0]-1)
        
        self.ans = 0
        self.dfs(adj, 0, -1)
        return self.ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		edges = []
		for _ in range(n-1):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.minimumEdgeRemove(n, edges)
		print(ans)

# } Driver Code Ends