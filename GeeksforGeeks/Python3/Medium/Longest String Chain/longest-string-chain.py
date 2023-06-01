#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def checkPossible(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) + 1:
            return False
        first = 0
        second = 0
        while first < len(s1):
            if second < len(s2) and s1[first] == s2[second]:
                first += 1
                second += 1
            else:
                first += 1
        if first == len(s1) and second == len(s2):
            return True
        return False
    
    @staticmethod
    def comp(s1: str, s2: str) -> bool:
        return len(s1) < len(s2)

    def longestChain(self, N, words):
        # Code here
        words.sort(key=len)
        dp = [1] * N
        maxi = 1
        for ind in range(N):
            for prev in range(ind):
                if self.checkPossible(words[ind], words[prev]) and 1 + dp[prev] > dp[ind]:
                    dp[ind] = 1 + dp[prev]
            if dp[ind] > maxi:
                maxi = dp[ind]
        return maxi

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        words = input().split()
        ob = Solution()
        res = ob.longestChain(N, words)
        print(res)
# } Driver Code Ends