#User function Template for python3
class Solution:
	def getCount(self, N):
		# code here
        neigh = [
            [0,8],
            [1,2,4],
            [1,2,3,5],
            [2,3,6],
            [1,4,5,7],
            [2,4,5,6,8],
            [3,5,6,9],
            [4,7,8],
            [5,7,8,9,0],
            [6,8,9]
        ]

        dp = [-1 for j in range(10)] 
        ans = [-1 for j in range(10)] 

        for i in range(10):
            ans[i] = 1 
        
        for n in range(2,N+1):
            for k in range(10):
                res = 0
                for i in neigh[k]:
                    res += ans[i]
                dp[k] = res
            ans = dp
            dp = [-1 for _ in range(10)] 

        return sum(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.getCount(N)
		print(ans)

# } Driver Code Ends