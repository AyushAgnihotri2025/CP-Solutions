#User function Template for python3
class Solution:
	def maximumDifferenceSum(self,arr, N):
		# code here
		dp = [[0]*2 for i in range(N)]
        for i in range(1,N):
            dp[i][0] = max(dp[i-1][0]+abs(arr[i]-arr[i-1]),dp[i-1][1]+abs(arr[i]-1))
            dp[i][1] = max(dp[i-1][0]+abs(1-arr[i-1]),dp[i-1][1])
        return max(dp[-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maximumDifferenceSum(arr,N)
		print(ans)
# } Driver Code Ends