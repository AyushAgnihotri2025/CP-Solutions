#User function Template for python3

class Solution:
    def getSpecialNumber(self, n):
        # code here 
        digits = []
        n -= 1
        while n:
            digits.append(n % 6)
            n //= 6
        ans = 0
        for d in reversed(digits):
            ans = (ans * 10 + d)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.getSpecialNumber(n))
# } Driver Code Ends