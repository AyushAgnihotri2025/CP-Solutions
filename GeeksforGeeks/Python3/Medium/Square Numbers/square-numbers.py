#User function Template for python3
import sys

sys.setrecursionlimit(10**9)

class Solution:
    def __init__(self):
        self.a = [True] * 100010
        self.primes = [0] * 100010
        self.in_ = 0
    
    def Sieve(self, n):
        self.a[1] = False
        for i in range(2, int(n**0.5)+1):
            if self.a[i]:
                for j in range(2*i, n+1, i):
                    self.a[j] = False
        for i in range(2, n+1):
            if self.a[i]:
                self.primes[self.in_] = i
                self.in_ += 1
    
    def calc(self, in_, cur, k):
        newCur = self.primes[in_] * self.primes[in_] * cur
        res = 0
        if newCur > k:
            return 0
        res += k // newCur
        res += self.calc(in_+1, cur, k)
        res -= self.calc(in_+1, newCur, k)
        return res
    
    def sqNum(self, N):
        # code here 
        self.Sieve(100000)
        ans = self.calc(0, 1, N)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.sqNum(N))
# } Driver Code Ends