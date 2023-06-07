#User function Template for python3

class Solution:
    def beautySum(self, s):
        # Code here
        ans = 0
        n = len(s)
        for i in range(n):
            d = {}
            d[s[i]] = 1
            for j in range(i+1,n):
                if s[j] in d:
                    d[s[j]] += 1
                else:
                    d[s[j]] = 1
                m = max(d.values())
                l = min(d.values())
                ans += m-l
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.beautySum(s))
# } Driver Code Ends