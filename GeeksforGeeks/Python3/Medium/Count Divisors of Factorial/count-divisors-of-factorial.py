#User function Template for python3

class Solution:
    def totalDivisors(self, N):
        # code here
        primes = [True] * (N + 1)
        prime_factors = []
        for i in range(2, N + 1):
            if primes[i]:
                j = i * i
                while j <= N:
                    primes[j] = False
                    j += i
                k = i
                count = 0
                while k <= N:
                    count += N // k
                    k *= i
                prime_factors.append(count)
        total_divisors = 1
        for count in prime_factors:
            total_divisors *= (count + 1)
        return total_divisors

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.totalDivisors(N))
# } Driver Code Ends