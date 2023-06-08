#User function Template for python3

import math

class Solution:
    def game (self, A, B):
        # code here
        if(A>B):
            temp = B
            B=A
            A=B
        k = B-A
        d = 1+math.sqrt(5)
        d = d/2
        d = d*k
        if(int(d)==A):
            return False
        else:
            return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N, K = map(int, input().split())
        ans = ob.game(N, K);
        if(ans):
            print("Dolly")
        else:
            print("Bunty")


# } Driver Code Ends