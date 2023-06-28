#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        n=N
        t=[0 for i in range(W+1)]
        for i in range(0,W+1):
            for j in range(n):
                if (i-wt[j])>=0:
                    t[i]=max(t[i],t[i-wt[j]]+val[j])
        return t[W]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends