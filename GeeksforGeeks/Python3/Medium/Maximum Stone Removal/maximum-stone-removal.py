#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxRemove(self, stones, n):
        # Code here
        rowlist = {}
        collist = {}
        for i in range(len(stones)):
            if stones[i][0] not in rowlist:
                rowlist[stones[i][0]] = []
            rowlist[stones[i][0]].append(i)
            if stones[i][1] not in collist:
                collist[stones[i][1]] = []
            collist[stones[i][1]].append(i)
        cc = 0
        vis = [False] * len(stones)
        for i in range(len(stones)):
            if not vis[i]:
                cc += 1
                self.dfs(stones, i, rowlist, collist, vis)
        return n - cc
    
    def dfs(self, stones, index, rowlist, collist, vis):
        vis[index] = True
        for val in rowlist[stones[index][0]]:
            if not vis[val]:
                self.dfs(stones, val, rowlist, collist, vis)
        for val in collist[stones[index][1]]:
            if not vis[val]:
                self.dfs(stones, val, rowlist, collist, vis)


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        adj = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.maxRemove(adj, n)
        print(res)
# } Driver Code Ends