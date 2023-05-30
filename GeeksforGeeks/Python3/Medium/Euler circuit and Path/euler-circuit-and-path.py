class Solution:
	def isEularCircuitExist(self, V, adj):
		#Code here
        c=0
        for i in range(V):
            if len(adj[i]) % 2 != 0:
                c+=1
        if c==0:
            return 2
        if c==2:
            return 1
        return 0


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEularCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends