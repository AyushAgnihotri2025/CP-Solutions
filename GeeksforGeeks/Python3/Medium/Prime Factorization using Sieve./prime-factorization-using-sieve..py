#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import math

class Solution:
    def sieve(self):
        pass
        
    def findPrimeFactors(self, N):
        # Code here
        primeFactors = []
        while N % 2 == 0:
            primeFactors.append(2)
            N //= 2
        sqrt_N = int(math.sqrt(N)) + 1
        for i in range(3, sqrt_N, 2):
            while N % i == 0:
                primeFactors.append(i)
                N //= i
        if N > 2:
            primeFactors.append(N)
        return primeFactors


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    ob = Solution()
    ob.sieve()
    for _ in range (t):
        n = int(input())
        ans = ob.findPrimeFactors(n)
        for v in ans:
            print(v, end = ' ')
        print()
# } Driver Code Ends