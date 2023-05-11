class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum, sum2=0, 0
        for i in range(n):
            sum+=a[i]
        for j in range(m):
            sum2+=b[j]
        
        a.sort()
        b.sort()
        
        i,j=0,0
        while(i<n and j<m):
            val=sum-(a[i])+(b[j])
            val2=sum2+(a[i])-(b[j])
            if val==val2:
                return 1
            if(val>val2):
                i+=1
            else:
                j+=1
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends