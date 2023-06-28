#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        # code here
        res=0
        f1=1
        f2=2
        f3=4
        if(n<=3):
            return 2**(n-1)
        for i in range(3,n):
            res=f1+f2+f3
            f1=f2
            f2=f3
            f3=res
        return res%((10**9)+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends