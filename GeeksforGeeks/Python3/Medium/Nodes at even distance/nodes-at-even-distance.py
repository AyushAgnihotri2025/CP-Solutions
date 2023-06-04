# User function Template for python3

from collections import deque

class Solution:
    def countOfNodes(self, graph,n):
        # code here
        dist = [-1 for _ in range(n+1)]
        dist[1] = 0
        q = deque()
        q.append((1, 0))
        while len(q) > 0:
            node, d = q.popleft()
            for nb in graph[node]:
                if dist[nb] == -1:
                    dist[nb] = d + 1
                    q.append((nb, d + 1))
        odd, even = 0, 0
        for i in range(1, n+1):
            if dist[i] % 2 == 1:
                odd += 1
            else:
                even += 1
        return odd * (odd - 1) // 2 + even * (even - 1) // 2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr = input().split()
        graph = defaultdict(list)
        for i in range(0,2*n-2,2):
            graph[int(arr[i])].append(int(arr[i+1]))
            graph[int(arr[i+1])].append(int(arr[i]))
            
            
        
        ob = Solution()
        print(ob.countOfNodes(graph,n))
# } Driver Code Ends