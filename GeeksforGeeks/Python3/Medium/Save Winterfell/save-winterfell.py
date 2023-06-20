#User function Template for python3
import sys
sys.setrecursionlimit(10000)
def dfs(adj, v, dist):
    for w, d in adj[v]:
        if dist[w] == -1:
            dist[w] = dist[v] + d
            dfs(adj, w, dist)
            
def longest_route (arr, n) : 
    #Complete the function
    adj = [[] for _ in range(n)]
    for e in arr:
        adj[e[0]-1].append((e[1]-1, e[2]))
        adj[e[1]-1].append((e[0]-1, e[2]))
    dist = [-1] * n
    dist[0] = 0
    dfs(adj, 0, dist)
    idx = max(enumerate(dist), key=lambda x: x[1])[0]
    dist = [-1] * n
    dist[idx] = 0
    dfs(adj, idx, dist)
    return max(dist)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
    
for _ in range(0,int(input())):
    n = int(input())
    arr = []
    for _ in range(0, n-1):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    res = longest_route(arr, n)
    print(res)






# } Driver Code Ends