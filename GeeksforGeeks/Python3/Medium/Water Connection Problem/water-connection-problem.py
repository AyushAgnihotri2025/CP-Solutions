#User function Template for python3

from collections import deque

class Solution:
    def solve(self, n, p ,a, b, d): 
        #code here
        visited=[False for _ in range(n)]
        graph=[[] for _ in range(n)]
        inV=[0 for _ in range(n)]
        outV=[0 for _ in range(n)]
        for i in range(p):
            graph[a[i]-1].append([b[i]-1,d[i]])
            outV[a[i]-1]+=1
            inV[b[i]-1]+=1
        answer=[]
        for i in range(n):
            if outV[i]!=1 or inV[i]!=0 or visited[i]:
                continue
            queue=deque()
            queue.append([i,float("inf")])
            e=i
            minPipe=float("inf")
            while queue:
                e,d=queue.popleft()
                if visited[e]:
                    continue
                visited[e]=True
                minPipe=min(minPipe,d)
                for v in graph[e]:
                    if not visited[v[0]]:
                        queue.append(v)
            if minPipe!=float("inf"):
                answer.append([i,e,minPipe])
        answer=[[x+1,y+1,z] for [x,y,z] in answer]
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        
        n,p = map(int,input().strip().split())
        a = []
        b = []
        d = []
        for i in range(p):
            x,y,z = map(int,input().strip().split())
            a.append(x)
            b.append(y)
            d.append(z)
            
        ob = Solution()
        ans = ob.solve(n, p, a, b, d)
        print(len(ans))
        for i in ans:
            print(str(i[0])+" "+str(i[1])+" "+str(i[2]))


# } Driver Code Ends