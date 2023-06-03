#User function Template for python3

class Solution:
    def reversedBits(self, X):
        # code here 
        d=(2**31)
        r=0
        while X>0:
            if X%2==1:
                r|=d
            d>>=1
            X>>=1
        return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends