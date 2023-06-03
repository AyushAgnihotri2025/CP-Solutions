#User function Template for python3
class Solution:
    def solve(self, k, n, d):
        if k == n - 1:
            num = 0
            for i in d:
                num = num * 10 + i
            if num % 17 == 0 and num > self.ans:
                self.ans = num
            return
        self.solve(k+1, n, d)
        for i in range(k+1, n):
            if d[i] != d[i-1]:
                d[i], d[k] = d[k], d[i]
                self.solve(k+1, n, d)
                d[i], d[k] = d[k], d[i]
        
    def largestDivisible (self, n):
        # code here 
        digits = [ord(c) - ord('0') for c in n]
        self.ans = -1
        sz = len(n)
        self.solve(0, sz, digits)
        if self.ans == -1:
            return "Not Possible"
        return str(self.ans)#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()

        ob = Solution()
        print(ob.largestDivisible(n))
# } Driver Code Ends