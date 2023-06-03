class Solution:
    def findMax(self,n, m,a, b, c):
        # Your code goes here
        d=dict()
        for i in range(n+1):
            d[i]=0
        for i in range(m):
            d[a[i]]=d[a[i]]+c[i]
            d[b[i]+1]=d[b[i]+1]-c[i]
        m=0
        s=0
        for i in range(n):
            if d.get(i)!=None:
                s=s+d[i]
                m=max(m,s)
        return m

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a=[]
        b=[]
        c=[]
        for j in range(0,m):
            v = list(map(int,input().split()))
            a.append(v[0])
            b.append(v[1])
            c.append(v[2])
        ob = Solution()
        print(ob.findMax(n,m,a,b,c))
# } Driver Code Ends