#User function Template for python3

class Solution:
    def solve(self, n, k, arr):
        # Code here
        def msum(start, end):
            if start > end:
                return 0
            
            if start == end:
                return arr[start]
            if dp[start][end] == -1:
                maxval = 0
                maxele = arr[start]
                for i, index in enumerate(range(start, min(end+1, start + k))):
                    maxele = max(maxele, arr[index])
                    part1sum = maxele * (i + 1)
                    part2sum = msum(index + 1, end)
                    maxval = max(maxval, part1sum + part2sum)
                dp[start][end] = maxval
            return dp[start][end]
            
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return msum(0, n - 1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k=input().split()
        n=int(n)
        k=int(k)
        arr= list(map(int, input().split()))
        ob = Solution()
        print(ob.solve(n, k, arr))
# } Driver Code Ends