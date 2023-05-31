#User function Template for python3

class Solution:
    def findString(self, s):
        # code here
        letters = [0]*26
        for char in s:
            letters[ord(char)-ord("A")] = 1
        max_start = None
        max_len = 1
        max_d = 0
        for start in range(25, -1, -1):
            if not letters[start]:
                continue
            for d in range(1, 26):
                cur_len = 1
                for check in range(start-d, -1, -d):
                    if not letters[check]:
                        break
                    cur_len += 1
                if cur_len > max_len or (cur_len == max_len and d < max_d):
                    max_len = cur_len
                    max_start = start
                    max_d = d
        res = ""
        i = max_start
        for _ in range(max_len):
            res += chr(i+ord("A"))
            i -= max_d
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.findString(s))
# } Driver Code Ends