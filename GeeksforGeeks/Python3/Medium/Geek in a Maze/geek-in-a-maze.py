#User function Template for python3
from collections import deque
def numberOfCells(n, m, r, c, u, d, mat):
    # code here
    def helper(i, j, u, d):
        if j > 0 and not (i, j-1) in visited:
            visited.add((i, j-1))
            helper(i, j-1, u, d)
        if j < m-1 and not (i, j+1) in visited:
            visited.add((i, j+1))
            helper(i, j+1, u, d)
        if u and i > 0 and not (i-1, j) in visited:
            visited.add((i-1, j))
            queue.append((i-1, j, u-1, d))
        if d and i < n-1 and not (i+1, j) in visited:
            visited.add((i+1, j))
            queue.append((i+1, j, u, d-1))
    if mat[r][c] == '#':
        return 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '#':
                visited.add((i, j))
    obstacles = len(visited)
    visited.add((r, c))
    queue = deque()
    queue.append((r, c, u, d))
    while queue:
        a, b, c, d = queue.popleft()
        helper(a, b, c, d)
    return len(visited) - obstacles


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(int(input()))

    for tcs in range(t):

        n, m, r, c, u, d = [int(x) for x in input().split()]

        mat = []

        for i in range(n):
            matele = [x for x in input()]
            mat.append(matele)

        print(numberOfCells(n, m, r, c, u, d, mat))
# } Driver Code Ends