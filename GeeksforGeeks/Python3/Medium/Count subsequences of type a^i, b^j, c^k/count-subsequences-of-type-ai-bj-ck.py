#User function Template for python3

class Solution:
    def fun(self,s):
        # code here
        arr = list(s)
        a = ab = abc = 0
        for i in range(len(arr)):
            if(arr[i] == 'a'):
                a = 2*a+1
            elif(arr[i] == 'b'):
                ab = 2*ab+a
            elif(arr[i] == 'c'):
                abc = 2*abc+ab
        return abc%1000000007


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Position this line where user code will be pasted.

t=int(input())
for _ in range(t):
    s=input()
    print(Solution().fun(s))
# } Driver Code Ends