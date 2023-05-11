#User function Template for python3

class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        trie = Trie()
        for s in dictionary:
            trie.insert(s)
        m, n = len(board), len(board[0])
        ans = set()
        def dfs(r, c, s, visited):
            nonlocal m, n, ans, trie
            if (r, c) in visited or r < 0 or r >= m or c < 0 or c >= n:
                return
            s += board[r][c]
            node = trie.search(s)
            if not node:
                return
            visited.add((r, c))
            if node.end:
                ans.add(s)
            for dr in (0, 1, -1):
                for dc in (0, 1, -1):
                    nr = r+dr
                    nc = c+dc
                    if (nr, nc) == (r, c):
                        continue
                    dfs(nr, nc, s, visited)
            visited.remove((r, c))
        for r in range(m):
            for c in range(n):
                dfs(r, c, "", set())
        return list(ans)

class Node:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, s):
        n = self.root
        for c in s:
            if c not in n.children:
                n.children[c] = Node()
            n = n.children[c]
        n.end = True
    
    def search(self, s):
        n = self.root
        for c in s:
            if not n:
                return False
            n = n.children.get(c)
        return n
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()                               # sorting output
        for i in found:
            print(i,end=' ')
        print()
# } Driver Code Ends