#User function Template for python3

class Solution:
    def satisfyEqn(self, a, n):
        # code here 
        d=dict()
        s=list()
        sum=0
        for i in range(n):
            for j in range(i+1,n):
                sum=a[i]+a[j]
                if sum not in d:
                    d[sum]=[i,j]
                else:
                   if i!=d[sum][0] and j!=d[sum][0] and i!=d[sum][1] and j!=d[sum][1]:
                       s.append([d[sum][0],d[sum][1],i,j])
        if len(s)==0:
            return [-1,-1,-1,-1]
        return min(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        ptr=ob.satisfyEqn(A,N)
        print(*ptr)
# } Driver Code Ends