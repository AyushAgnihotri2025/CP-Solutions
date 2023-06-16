#User function Template for python3

class Solution:
    def largePrime(self, n):
        # code here
        i = 2
        d = {}
        while i*i <= n:
            while n%i == 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
                n = n//i
            i += 1
        if n>1: 
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        if d == {}:
            return 0
        if d[max(d)] > 1:
            return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        if ob.largePrime(n) == 1:
            print("YES")
        else:
            print("NO")
# } Driver Code Ends