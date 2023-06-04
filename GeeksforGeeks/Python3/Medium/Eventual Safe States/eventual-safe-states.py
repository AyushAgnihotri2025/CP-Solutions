#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        adj_r=[[]for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                adj_r[j].append(i)
        indegree={}
        for i in range(V):
            indegree[i]=0
        for i in adj_r:
            for j in i:
                indegree[j]+=1
        q=[]
        for i in indegree:
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            pop=q.pop()
            res.append(pop)
            for i in adj_r[pop]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        res.sort()
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends