#User function Template for python3

class Solution:
    def CountSpecialPalindrome(self, S):
        # code here
        ans = 0
        n = len(S)
        i = 1
        while i < n:
            j = i - 1
            if S[i] == S[j]:
                while i < n and S[i] == S[j]:
                    i += 1
                if i - j > 1:
                    ans += (i - j) * (i - j - 1) // 2
            else:
                k = i
                j = 1
                c = ' '
                while k - j >= 0 and k + j < n:
                    if S[k-j] == S[k+j] and (c == ' ' or c == S[k-j]):
                        ans += 1
                        c = S[k-j]
                        j += 1
                    else:
                        break
                i += 1
        return ans 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.CountSpecialPalindrome(S))
# } Driver Code Ends