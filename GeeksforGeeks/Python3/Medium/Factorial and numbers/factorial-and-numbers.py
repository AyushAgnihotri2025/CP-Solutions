#User function Template for python3
import math
from collections import defaultdict
class Solution:
    def helper(self, mi, k, v):
        ans = 0
        while mi > 0:
            ans += mi // k
            mi //= k
            if ans >= v:
                return True
        return ans >= v
    def search(self, k, v):
        lo, hi = 1, 1000001
        ans = 0
        while lo <= hi:
            mi = (lo + hi) // 2
            if self.helper(mi, k, v):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans
	def findFact(self, num):
		# Code here
		if num == 1:
            return 1
        d = defaultdict(int)
        for i in range(2, int(math.sqrt(num))+1):
            while num % i == 0:
                d[i] += 1
                num //= i
        if num != 1:
            d[num] = 1
        ans = 0
        for k, v in d.items():
            if v == 1:
                ans = max(ans, k)
            else:
                ans = max(ans, self.search(k, v))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		obj = Solution()
		ans = obj.findFact(n)
		print(ans)

# } Driver Code Ends