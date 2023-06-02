#User function Template for python3

class Solution:
    def tiny_miny (self, a, n):
        # Complete the function
        y = ""
        for i in range(1,n+1):
            y += str(a**i)
        return "".join(sorted(y.replace("0","")))

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    a, n = map(int , input().split())
    ob=Solution()
    res = ob.tiny_miny(a, n)
    print(res)


# } Driver Code Ends