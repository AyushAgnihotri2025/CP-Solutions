#User function Template for python3
from functools import lru_cache
class Solution:
	def findProb(self, N, start_x, start_y, steps):
		# Code here
		dir = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
		@lru_cache(None)
        def solve(x,y,t):
            if not (0<=x<N and 0<=y<N):
                return 0
            if t==0:
                return 1
            ans=0
            for i,j in dir :
                ans+=solve(x+i,y+j,t-1)
            return ans
        return solve(start_x,start_y,steps)/8**steps


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, start_x, start_y, steps = input().split()
		N = int(N)
		start_x = int(start_x)
		start_y = int(start_y)
		steps = int(steps)
		ob = Solution()
		ans = ob.findProb(N, start_x, start_y, steps)
		print('%.6f'%ans)
# } Driver Code Ends