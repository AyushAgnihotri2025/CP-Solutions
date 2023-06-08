#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def Solve(self, n, adj):
        # Code here
        self.parent = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]

        def findP(node):
            if self.parent[node]==node:
                return node
            self.parent[node] = findP(self.parent[node])
            return self.parent[node]

        def union(u,v):
            u_p = findP(u)
            v_p = findP(v)
            if self.size[u_p]<self.size[v_p]:
                self.parent[u_p]=v_p
                self.size[v_p]+=self.size[u_p]
            else:
                self.parent[v_p]=u_p
                self.size[u_p]+=self.size[v_p]

        extra_ed = 0
        used_ed = 0
        for u,v in adj:
            if findP(u)==findP(v):
                extra_ed+=1
            else:
                used_ed+=1
                union(u,v)
        node_in_mst = used_ed+1
        if extra_ed>=(n-node_in_mst):
            return n-node_in_mst
        return -1

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        adj = [list(map(int, input().split())) for _ in range(m)]
        ob = Solution()
        res = ob.Solve(n, adj)
        print(res)
# } Driver Code Ends