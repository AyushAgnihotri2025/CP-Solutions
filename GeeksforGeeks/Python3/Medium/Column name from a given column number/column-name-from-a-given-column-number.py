#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        ans = ""
        while n:
            ans = chr(65+(n-1)%26)+ans
            n = (n-1)//26
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends