#User function Template for python3
import math
from typing import List

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        adj = [[] for _ in range(n)]
        for s,d,cost in flights:
            adj[s].append([d,cost])
        queue = []
        dist = [math.inf for _ in range(n)]
        queue.append((0,src,0))
        while queue:
            stops, node, dis = queue.pop(0)
            if stops > k:
                continue
            for adjNode, cost in adj[node]:
                newDist = dis+cost
                if newDist < dist[adjNode] and stops<=k:
                    dist[adjNode] = newDist
                    queue.append((stops+1, adjNode, newDist))
        if dist[dst]==math.inf:
            return -1
        return dist[dst]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,edge=map(int,input().split())
        flights=[]
        for _ in range(edge):
            temp=list(map(int,input().split()))
            flights.append(temp[:])
        src=int(input())
        dst=int(input())
        k=int(input())
        obj=Solution()
        res=obj.CheapestFLight(n,flights,src,dst,k)
        print(res)

        
        
# } Driver Code Ends