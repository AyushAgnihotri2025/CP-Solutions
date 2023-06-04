#User function Template for python3

import heapq

class Solution:
    def minTime(self, dependency, duration, n, m):
        #code here
        degree = [0] * n
        adj = [[] for _ in range(n)]
        for edge in dependency:
            adj[edge[0]].append(edge[1])
            degree[edge[1]] += 1
        dist = [-1] * n
        pq = []
        for i in range(n):
            if degree[i] == 0:
                dist[i] = duration[i]
                heapq.heappush(pq, (dist[i], i))
        while len(pq) > 0:
            d, v = heapq.heappop(pq)
            for w in adj[v]:
                degree[w] -= 1
                if degree[w] == 0:
                    dist[w] = d + duration[w]
                    heapq.heappush(pq, (dist[w], w))
        if -1 in dist:
            return -1
        return max(dist)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,m= map(int,input().split())
    duration = list(map(int,input().split()))
    dependency = []
    for i in range(0,m):
        l = list(map(int,input().split()))
        dependency.append(l)
    obj = Solution()
    print(obj.minTime(dependency,duration,n,m))
# } Driver Code Ends