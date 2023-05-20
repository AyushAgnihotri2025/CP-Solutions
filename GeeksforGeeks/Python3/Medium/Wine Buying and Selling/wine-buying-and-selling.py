#User function Template for python3


class Solution:	
	def wineSelling(self, Arr, N):
		# code here
		count, ans = 0, 0
		for i in Arr:
		    ans += abs(count)
		    count += i
		return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        Arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.wineSelling(Arr,N)
        
        print(ans)

# } Driver Code Ends