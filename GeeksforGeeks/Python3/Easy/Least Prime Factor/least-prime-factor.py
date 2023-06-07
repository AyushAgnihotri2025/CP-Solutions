#User function Template for python3
import math

class Solution:
    def leastPrimeFactor (self, n):
        # code here
        ans = [0, 1]
        smallest_prime = [0] * (n+1)
        smallest_prime[1] = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if smallest_prime[i] == 0:
                for j in range(i*i, n+1, i):
                    if smallest_prime[j] == 0:
                        smallest_prime[j] = i
        for i in range(2, n+1):
            if smallest_prime[i] == 0:
                smallest_prime[i] = i
        for i in range(2, n+1):
            ans.append(smallest_prime[i])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends