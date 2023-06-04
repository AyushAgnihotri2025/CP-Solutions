#User function Template for python3
class Solution:
    def sumOfDigits (self,N):
        # code here
        s = 0
        for i in range(N+1):
            while(i>0):
                s += i%10
                i //= 10
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends