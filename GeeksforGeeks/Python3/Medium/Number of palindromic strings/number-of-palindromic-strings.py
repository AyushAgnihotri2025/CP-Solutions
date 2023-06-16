#User function Template for python3
class Solution:
	def palindromicStrings(self, N, K ):
		# code here
		mod = 10**9+7
        sumi = 0
        t = 1
        for i in range(1, N+1):
            t = 1
            if i%2==0:
                t2 = i//2
            else:
                t2 = i//2+1
            for j in range(t2):
                t *= (K-j)
                t%=mod
            sumi+=t
            sumi%=mod
        return sumi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,k = input().split()
		n,k = int(n), int(k)

		ob = Solution()
		answer = ob.palindromicStrings(n,k)
		print(answer)

# } Driver Code Ends