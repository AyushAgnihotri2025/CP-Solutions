#User function Template for python3


class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
        dp = [-1 for i in range(n+1)]
        dp[0] = arr[0]
        dp[1] = arr[0]+arr[1]
        dp[2] = max(arr[1]+arr[2], max(arr[2]+arr[0],arr[1]))
        for i in range(3,n):
            incl1 = arr[i]+dp[i-2]
            incl2 = arr[i]+arr[i-1]+dp[i-3]
            excl = dp[i-1]
            dp[i] = max(incl1,max(incl2,excl))
        return dp[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends