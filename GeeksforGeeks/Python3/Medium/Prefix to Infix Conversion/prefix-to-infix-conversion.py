#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def isOperand(self, char):
        return char not in "+-*/^"
    def preToInfix(self, pre_exp):
        # Code here
        stack = []
        for i in range(len(pre_exp) - 1, -1, -1):
            charNow = pre_exp[i]
            
            if self.isOperand(charNow):
                stack.append(charNow)
            else:
                firstOperand =  stack.pop()
                secondOperand = stack.pop()
                
                combinedOperand = "(" + firstOperand + charNow + secondOperand + ")"
                
                stack.append(combinedOperand)
            
        return stack[-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        prefix = input()
        ob = Solution()
        res = ob.preToInfix(prefix)
        print(res)
# } Driver Code Ends