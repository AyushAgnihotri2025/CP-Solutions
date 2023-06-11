#User function Template for python3

class Solution:
    def maxCoins(self, A, B, T, N):
        # code here
        r=[]
        u=T
        l=0
        for i in range(N):
            r.append((B[i],A[i]))
        r.sort()
        r.reverse()
        for i in r:
            if u == 0:
                return l
            if i[1]<u:
                l=l+(i[0]*i[1])
                u=u-i[1]
            elif i[1]>=u:
                l=l+(i[0]*u)
                u=0
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        T,N=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxCoins(A,B,T,N))
# } Driver Code Ends