#User function Template for python3

class Solution:
	def fractionToDecimal(self, numerator, denominator):
		# Code here
        def _tostr(lst): return ''.join( lst )
        v, ints = numerator%denominator, numerator//denominator
        dec, flag = [], {}
        repeat = -1 # repeat start ind
        bit = 0
        while v and v not in flag:
            flag[v] = bit
            bit += 1
            v *= 10
            dec.append(str(v // denominator))
            v = v % denominator
            
        if v in flag: repeat = flag[v]
        if not dec: return str(ints)
        if repeat == -1: return str(ints) + "." + _tostr(dec)
        return str(ints) + '.' + _tostr(dec[:repeat]) + '(' + _tostr(dec[repeat:])  + ')'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		numerator, denominator = input().split()
		numerator = int(numerator); denominator = int(denominator)
		ob = Solution()
		ans = ob.fractionToDecimal(numerator, denominator)
		print(ans)
# } Driver Code Ends