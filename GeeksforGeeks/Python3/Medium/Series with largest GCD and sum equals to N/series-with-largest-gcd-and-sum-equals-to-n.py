#User function Template for python3

import math

class Solution:
	def M_sequence(self, N, M):
		# code here
		cnt = (1 + M) * M // 2
        mgcd = -1
        for i in range(int(math.sqrt(N)), 0, -1):
            if N % i == 0:
                d = N // i
                if d * cnt <= N:
                    mgcd = max(mgcd, d)
                if i * cnt <= N:
                    mgcd = max(mgcd, i)
        if mgcd == -1:
            print(-1)
            return []
        ans = []
        i = 1
        while len(ans) < M - 1:
            ans.append(i * mgcd)
            N -= i * mgcd
            i += 1
        ans.append(N)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,M = input().split()
		N=int(N)
		M=int(M)
		ob = Solution();
		ans = ob.M_sequence(N,M)
		for i in range(len(ans)):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends