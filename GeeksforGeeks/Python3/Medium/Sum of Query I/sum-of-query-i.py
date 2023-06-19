#User function Template for python3

class Solution:
	def FindQuery(self, nums, Query):
		# Code here
        mod =1000000007
		n = len(nums)
        m = len(Query)
        dp1 = [0 for i in range(n+1)]
        dp2 = [0 for i in range(n+1)]
        dp3 = [0 for i in range(n+1)]
        for i in range(1,n+1):
            dp1[i] = (dp1[i-1] + nums[i-1]) % mod;
            dp2[i] = (dp2[i-1] + i * nums[i-1] ) % mod;
            dp3[i] = (dp3[i-1] + i* i *nums[i-1])% mod;
        rst = []
        for query in Query:
            start = query[0]
            end = query[1]
            ans = 0
            ans = dp3[end] - dp3[start-1] 
            ans +=(start-1) * (start-1) * (dp1[end] - dp1[start-1])
            ans += 2 * (1-start) * (dp2[end] - dp2[start-1])
            ans = ans % mod
            rst.append(int(ans))
        return rst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		q = int(input())
		Query = []
		for i in range(q):
			Query.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.FindQuery(nums, Query)
		for _ in ans:
			print(_)


# } Driver Code Ends