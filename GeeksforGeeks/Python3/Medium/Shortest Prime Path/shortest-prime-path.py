#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def solve (self,Num1,Num2):
        #code here
        v=[1 for _ in range(10000)]
        p = 2
        n=10000
        while (p * p <= n):
            if (v[p] == 1):
                for i in range(p * p, n, p):
                    v[i] = 0
            p += 1
        ans=0
        v[Num1]=0

        def ss(x):
            s=str(x)
            t=[]
            for i in range(4):
                for new in range(10):        
                    y=s[:i]+str(new)+s[i+1:]
                    if y[0]!='0' and y!=s and v[int(y)]==1:
                        v[int(y)]=0
                        t.append(int(y))
            return(t)

        ans=0
        q=[Num1]
        while q:
            q1=[]
            for val in q:
                new=ss(val)
                for child in new:
                    if child==Num2:
                        return(ans+1)
                    q1.append(child)
            q=q1
            ans+=1
        return(ans)


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        Num1,Num2=map(int,input().split())
        ob = Solution()
        print(ob.solve(Num1,Num2))
# } Driver Code Ends