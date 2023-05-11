#User function Template for python3
class Solution:
    def valid(self, s): 
        #code here
        stack = []
        for e in s:
            if len(stack) == 0 or e == '(' or e == '{' or e == '[':
                stack.append(e)
            else:
                if stack[-1] == '(' and e == ')':
                    stack.pop()
                elif stack[-1] == '{' and e == '}':
                    stack.pop()
                elif stack[-1] == '[' and e == ']':
                    stack.pop()
                else:
                    stack.append(e)
        return len(stack) <= 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        if ob.valid(s):
            print(1)
        else:
            print(0)
# } Driver Code Ends