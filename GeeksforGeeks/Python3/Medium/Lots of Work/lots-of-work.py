#User function Template for python3
class Solution:
    def check(self, a, n, d, v):
        cnt = 0
        curr = 0
        for i in range(n):
            if curr + a[i] > v:
                curr = a[i]
                cnt += 1
            else:
                curr += a[i]
        return cnt + 1 <= d
        
    def minAmountOfTime(self, Arr, n, m):
        # code here
        lo, hi = max(Arr), sum(Arr)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.check(Arr, n, m, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n=int(n)
		m=int(m)
		Arr = input().split()
		for itr in range(n):
		    Arr[itr] = int(Arr[itr])
		ob=Solution()
		print(ob.minAmountOfTime(Arr, n, m))
# } Driver Code Ends