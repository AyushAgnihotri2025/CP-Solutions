#User function Template for python3
class Solution:
	def findMaxSum(self,arr, n):
		# code here
		dp = [[0 for i in range(2)] for i in range(n)]
        dp[n-1][1] = arr[n-1]
        for index in range(n-2,-1,-1):
            for call in range(2):
                np = dp[index+1][1]
                pick = -1e9
                if call:
                    pick = dp[index+1][0] + arr[index]
                dp[index][call] =  max(pick,np)
        return max(dp[0][1],dp[0][0])

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