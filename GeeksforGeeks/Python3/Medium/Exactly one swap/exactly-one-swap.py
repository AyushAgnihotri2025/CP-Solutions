#User function Template for python3
class Solution:
    def countStrings(self, S): 
        #code here
        ans = 0
        dict = {}
        n = len(S)
        any = 0
        for i in range(n):
            if not S[i] in dict:
                dict[S[i]] = 1
                ans += i
            else:
                any = 1
                ans += i - dict[S[i]]
                dict[S[i]] += 1
        return ans + any
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countStrings(S)
        print(ans)
# } Driver Code Ends