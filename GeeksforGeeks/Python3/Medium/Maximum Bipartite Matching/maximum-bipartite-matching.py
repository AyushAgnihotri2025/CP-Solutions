#User function Template for python3

class Solution:
	def maximumMatch(self, G):
		# code here
        applicants = len(G)
        jobs = len(G[0])
        res = 0
        match = [-1]*jobs
        for i in range(applicants):
            seen = [False]*(jobs)
            if self.dfs(G, seen, match, i, applicants, jobs):
                res+=1
        return res

    def dfs(self, g, seen, match, u, applicants, jobs):
        for v in range(jobs):
            if g[u][v] == 1 and seen[v] == False:
                seen[v] = True
                if match[v] == -1 or self.dfs(g, seen, match, match[v], applicants, jobs):
                    match[v] = u
                    return True
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m, n = map(int, input().strip().split())
		G = []
		for i in range(m):
			G.append(list(map(int, input().strip().split())))
		obj = Solution()
		ans = obj.maximumMatch(G)
		print(ans)
# } Driver Code Ends