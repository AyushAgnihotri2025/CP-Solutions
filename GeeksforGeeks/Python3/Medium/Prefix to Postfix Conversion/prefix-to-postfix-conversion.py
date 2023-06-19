#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        s=[]
        for i in pre_exp[::-1]:
            if i.isalpha():
                s.append(i)
            else:
                a=s.pop(-1)
                b=s.pop(-1)
                s.append(a+b+i)
        return s[-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        prefix = input()
        ob = Solution()
        res = ob.preToPost(prefix)
        print(res)
# } Driver Code Ends