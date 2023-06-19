#User function Template for python3
class Solution:
	def countDivisibleSubseq(self, s, N):
		# code here
		MOD = 10 ** 9 + 7
        def rec(index, rem):
            if index == len(s):
                return int(rem == 0)
            nt = rec(index + 1, rem)
            tk = rec(index + 1, (rem * 10 + int(s[index])) % N)
            return nt + tk
        dp = [[-1 for _ in range(N + 1)] for _ in range(len(s) + 1)]
        def mem(index, rem):
            if index == len(s):
                return int(rem == 0)
            if dp[index][rem] != -1:
                return dp[index][rem]
            nt = mem(index + 1, rem)
            tk = mem(index + 1, (rem * 10 + int(s[index])) % N)
            dp[index][rem] = nt + tk
            return dp[index][rem]
        return mem(0, N) % MOD
        return rec(0, N) % MOD


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		n = int(input())
		ob = Solution()
		ans = ob.countDivisibleSubseq(s,n)
		print(ans)

# } Driver Code Ends