#User function Template for python3
import math

class Solution:
    def sumOfNaturals(self, n):
        # code here 
        return int(((n*(n+1))//2)%(math.pow(10,9)+7))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfNaturals(n))
# } Driver Code Ends