#User function Template for python3

class Solution:
    def countSubstring(self, s):
        # Code here
        n = len(s)
        j = 0
        a, b, c = 0, 0, 0
        ans = 0
        for i in range(n):
            if s[i] == 'a':
                a += 1
            elif s[i] == 'b':
                b += 1
            else:
                c += 1
            while a > 0 and b > 0 and c > 0:
                ans += n - i
                if s[j] == 'a':
                    a -= 1
                elif s[j] == 'b':
                    b -= 1
                else:
                    c -= 1
                j += 1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.countSubstring(s))
# } Driver Code Ends