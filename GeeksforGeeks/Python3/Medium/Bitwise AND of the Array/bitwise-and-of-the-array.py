#User function Template for python3
class Solution:
    def count(self, N, A, X): 
        # code here
        prefix = 0
        ans = N
        for i in range(30, -1, -1):
            if X & (1 << i):
                prefix |= 1 << i
                continue
            cnt = 0
            prefix |= 1 << i
            for a in A:
                if (a & prefix) == prefix:
                    cnt += 1
            ans = min(ans, N - cnt)
            prefix ^= 1 << i
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(N, A, X)
        print(ans)
# } Driver Code Ends