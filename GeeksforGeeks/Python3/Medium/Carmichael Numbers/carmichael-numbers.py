#User function Template for python3

from math import gcd

class Solution:
    def binpow(self, a, b, n):
        ans = 1
        while b:
            if b & 1:
                ans = (ans * a) % n
            a = (a * a) % n
            b >>= 1
        return ans
        
    def isCarmichael(self, n):
        # code here
        for b in range(1, n+1):
            if gcd(b, n) == 1 and self.binpow(b, n-1, n) != 1:
                return 0
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        flag = ob.isCarmichael(n)
        if flag == 1:
            print("Yes")
        else:
            print("No")
# } Driver Code Ends