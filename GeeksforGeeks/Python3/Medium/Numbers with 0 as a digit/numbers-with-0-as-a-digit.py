#User function Template for python3

class Solution:
    def countZero (self, N):
        #complete the function here
        cnt = [0] * 7
        d = 9
        for i in range(1, 7):
            cnt[i] = d
            d *= 9
        total = [0] * 7
        total[0] = cnt[0]
        for i in range(1, 7):
            total[i] = total[i-1] + cnt[i]
        s = str(N)
        n = len(s)
        ans = total[n-1]
        zero = False
        for i in range(n):
            if s[i] != '0':
                ans += (int(s[i]) - 1) * cnt[n-1-i]
            else:
                zero = True
                break
        if not zero:
            ans += int(s[n-1])
        return N - ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.countZero(n))
# } Driver Code Ends