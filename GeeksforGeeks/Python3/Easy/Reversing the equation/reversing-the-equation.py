#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        res = ""
        n = len(s)
        i = n - 1
        st = []
        while i >= 0:
            if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
                while len(st) > 0:
                    res += st.pop()
                res += s[i]
            else:
                st.append(s[i])
            i -= 1
        while len(st) > 0:
            res += st.pop()
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends