#User function Template for python3

class Solution:
    def cuts(self, s):
        n = len(s)
        zero = ord('0')
        dp = [0] * n
        
        def isPowerOf(num, base):
            while num > 1:
                if num % base != 0:
                    return False
                num //= base
            
            return True
            
        if ord(s[-1]) - zero == 0:
            dp[-1] = -1
        else:
            dp[-1] = 1
        
        
        for i in range(n - 2, -1, -1):
            if (ord(s[i]) - zero) == 0:
                dp[i] = -1
                continue
            
            val = 0
            dp[i] = float('inf')
            
            for j in range(i, n):
                val = val * 2 + (ord(s[j]) - zero)
                
                if isPowerOf(val, 5):
                    if j == n - 1:
                        dp[i] = 1
                    elif dp[j + 1] != -1:
                            dp[i] = min(dp[i], dp[j + 1] + 1)
                            
            if dp[i] == float('inf'):
                dp[i] = -1
        
        return dp[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.cuts(s))

# } Driver Code Ends