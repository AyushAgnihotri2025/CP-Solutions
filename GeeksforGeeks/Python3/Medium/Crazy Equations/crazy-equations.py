#User function Template for python3
class Solution:
	def distinctValues(self, n, a, b, c, d):
		# code here
		arr = [a+b, a+c, c+d, b+d]
        arr.sort()
        diff = arr[-1] - arr[0]
        ans = 0
        return max(n - diff, 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,a,b,c,d = input().split()
		n=int(n)
		a=int(a)
		b=int(b)
		c=int(c)
		d=int(d)
		ob = Solution();
		print(ob.distinctValues(n,a,b,c,d))

# } Driver Code Ends