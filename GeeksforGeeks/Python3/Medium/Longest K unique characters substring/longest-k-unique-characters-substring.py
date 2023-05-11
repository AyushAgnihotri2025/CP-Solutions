#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        map = {}
        left = 0
        maxLength = -1
        for right in range(len(s)):
            ch = s[right]
            map[ch] = map.get(ch, 0) + 1
            if len(map) == k:
                maxLength = max(maxLength, right - left + 1)
            while len(map) > k:
                left_char = s[left]
                map[left_char] -= 1
                if map[left_char] == 0:
                    del map[left_char]
                left += 1
        return maxLength


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends