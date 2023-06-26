#User function Template for python3

class Solution:
	def NthDigit(self, n):
		# Code here
		if n <= 9:
            return n
        count = [0] * 10
        count[1] = 10
        t = 90
        for i in range(2, 10):
            count[i] = i * t
            t *= 10
        j = -1
        for i in range(1, 10):
            if n <= count[i]:
                j = i
                break
            else:
                n -= count[i]
        p, q = n // j, n % j
        s = 10 ** (j - 1) + p
        return str(s)[q]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthDigit(n)
		print(ans)
# } Driver Code Ends