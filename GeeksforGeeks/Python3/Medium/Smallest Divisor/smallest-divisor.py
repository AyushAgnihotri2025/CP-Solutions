#User function Template for python3
from math import ceil

class Solution:
    def smallestDivisor(self, nums, K):
        # Code here
        i=1
        j=max(nums)+1
        def check(divisor):
            return sum(ceil(num / divisor) for num in nums) <= K
        while i<j:
            mid=(i+j)//2
            if check(mid):
                j=mid
            else:
                i=mid+1
        return j

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, K = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.smallestDivisor(nums, K)
        print(res)
# } Driver Code Ends