#User function Template for python3

class Solution:
    def minSubset(self, A,N):
        A.sort(reverse=True)
        sum2 = sum(A)
        sum1 = 0
        count = 0
        for i in range(N):
            sum1 = sum1+A[i]
            sum2 = sum2-A[i]
            count += 1
            if sum1>sum2:
                break
        return count
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSubset(A,N)
        print(ans)
# } Driver Code Ends