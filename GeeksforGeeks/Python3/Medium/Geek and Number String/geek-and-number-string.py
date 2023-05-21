#User function Template for python3

class Solution:
    def minLength(self, s, n): 
        #code here 
        setti = set(['12', '21', '34', '43', '56', '65', '78', '87', '90', '09'])
        stack = []
        for item in s:
            if stack and stack[-1] + item in setti:
                stack.pop()
            else:
                stack.append(item)
        return len(stack)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        ob = Solution()
        print(ob.minLength(s,n))
# } Driver Code Ends