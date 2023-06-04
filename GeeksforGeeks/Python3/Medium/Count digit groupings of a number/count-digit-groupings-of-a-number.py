#User function Template for python3

from functools import lru_cache

class Solution:
	def TotalCount(self, s):
		# Code here
        n = len(s)
        sums = [[0]*n for _ in range(n)]
        for r in range(n-1, -1, -1):
            for l in range(r, -1, -1):
                if l == r:
                    sums[l][r] = int(s[l])
                else:
                    sums[l][r] = int(s[l]) + sums[l+1][r]
        @lru_cache(None)
        def count(n, start, s):
            if len(s[start:]) == 0:
                return 1
                
            cnt = 0
            for i in range(start+1, len(s)+1):
                nxt_n = sums[start][i-1] 
                if nxt_n >= n:
                    cnt += count(nxt_n, i, s)
            return cnt
        return count(0, 0, s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends