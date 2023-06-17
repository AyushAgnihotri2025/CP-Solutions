#User function Template for python3

class Solution:
    def specialXor(self, N, Q, a, query):
        # code here
        for i in range(1,len(a)):
            a[i] ^= a[i-1]
        return [a[-1]^(a[r-1]^(a[l-2] if l-2 >= 0 else 0)) for l,r in query]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 
sys.setrecursionlimit(10**5) 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, Q = map(int,input().strip().split())
        a = list(map(int, input().strip().split()))
        query = [[0 for j in range(2)] for i in range(Q)]
        for i in range(Q):
            l, r = map(int,input().strip().split())
            query[i][0] = l
            query[i][1] = r
        
        ob = Solution()
        ans = ob.specialXor(N, Q, a, query)
        for i in ans:
            print(i)
# } Driver Code Ends