#User function Template for python3

class Solution:
    def countPairs(self,X, Y, m, n):
        # code here
        for i in range(m):
            X[i]**=1/X[i]
        for i in range(n):
            Y[i]**=1/Y[i]
        X.sort()
        Y.sort()
        i=j=0
        ans=0
        while i<m:
            if j==n:
                ans+=n
            else:
                while j<n and X[i]>Y[j]:
                    j+=1
                ans+=j
            i+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        m, n = list(map(int, input().strip().split()))
        X = list(map(int, input().strip().split()))
        Y = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairs(X, Y, m, n)
        print(ans)
        tc -= 1

# } Driver Code Ends