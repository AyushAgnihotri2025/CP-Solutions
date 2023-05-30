class Solution:
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		#Code here
        main = set()
        def dfs(root):
            if visited[root] == 1:return
            visited[root] = 1
            main.add(root)
            for i in adj[root]:
                dfs(i)
        for i in range (V):
            visited = [0] * V
            if i not in main:
                dfs(i)
                if sum(visited) == V:return i
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends