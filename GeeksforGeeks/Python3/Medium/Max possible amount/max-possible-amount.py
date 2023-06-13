#User function Template for python3
class Solution:
    def solve(self, arr, n, dp, st, ed):
        if st > ed:
            return 0
        if dp[st][ed] != -1:
            return dp[st][ed]
        a = arr[st] + min(self.solve(arr, n, dp, st+2, ed), self.solve(arr, n, dp, st+1, ed-1))
        b = arr[ed] + min(self.solve(arr, n, dp, st, ed-2), self.solve(arr, n, dp, st+1, ed-1))
        dp[st][ed] = max(a, b)
        return dp[st][ed]

    def maxAmount(self, arr, n):
        # code here
        dp = [[-1 for i in range(n)] for j in range(n)]
        ans = self.solve(arr, n, dp, 0, n-1)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxAmount(Arr, N)
		print(ans)




# } Driver Code Ends