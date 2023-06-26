#User function Template for python3

class Solution:
    def findpos(self, n):
        # code here
        cnt = [0] * 51
        for i in range(1, 51):
            cnt[i] = 2 ** i
        total = cnt.copy()
        for i in range(1, 51):
            total[i] += total[i-1]
        sz = len(n)
        ans = total[sz-1]
        for i in range(sz - 1):
            if n[i] == '7':
                ans += cnt[sz-1-i]
        ans += 1 if n[-1] == '4' else 2
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = input()

        solObj = Solution()

        ans = solObj.findpos(n)

        print(ans)
# } Driver Code Ends