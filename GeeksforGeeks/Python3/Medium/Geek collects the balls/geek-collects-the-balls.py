#User function Template for python3

class Solution:
    def maxBalls(self, N, M, a, b):
        # code here
        i=0
        j=0
        val1,val2=0,0
        x,y=0,0
        while(i<N and j<M):
            x,y=a[i],b[j]
            if (x<y):
                val1=val1+x
                i=i+1
    
            elif(y<x):
                val2=val2+y
                j=j+1
                
            else:
                x1,y1=0,0
                while(i<N and a[i]==x):
                    x1=x1+x
                    i=i+1
                while(j<M and b[j]==y):
                    y1=y1+y
                    j=j+1
    
                val1,val2=max(val1+x1,val1+x1+y1-(2*x),val2+x1+y1-x),max(val2+y1,val2+x1+y1-(2*x),val1+x1+y1-x)
        while(i<N):
            val1=val1+a[i]
            i=i+1
        while(j<M):
            val2=val2+b[j]
            j=j+1
        ans=max(val1,val2)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        a = input().split()
        b = input().split()
        for i in range(N):
            a[i] = int(a[i])
        for i in range(M):
            b[i] = int(b[i])
        
        ob = Solution()
        print(ob.maxBalls(N, M, a, b))
# } Driver Code Ends