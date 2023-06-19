#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        stack = []
        for i in range(len(post_exp)):
            if post_exp[i].isalpha():
                stack.append(post_exp[i])
            else:
                next = stack.pop()
                prev = stack.pop()
                cur = post_exp[i] + prev + next
                stack.append(cur)
        return stack[0]   

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToPre(postfix)
        print(res)
# } Driver Code Ends