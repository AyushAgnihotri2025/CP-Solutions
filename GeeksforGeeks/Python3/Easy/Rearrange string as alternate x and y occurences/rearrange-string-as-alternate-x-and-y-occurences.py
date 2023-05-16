#User function Template for python3

class Solution:
    def arrangeString(self, s, x, y):
        # code here
        zeros = 0
        ones = 0
        for item in s:
            zeros += item == '0'
            ones += item == '1'
        output = ''
        while ones and zeros:
            i = 0
            while i < x and zeros:
                output += '0'
                i += 1
                zeros -= 1
            i = 0
            while i < y and ones:
                output += '1'
                i += 1
                ones -= 1
        return output + zeros * '0' + ones * '1'

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x,y = input().strip().split(" ")
        x,y = int(x), int(y)
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s,x,y)
        print(ans)
# } Driver Code Ends