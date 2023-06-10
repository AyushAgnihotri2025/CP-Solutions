#User function Template for python3
class Solution:
    def costOfSweets (self, M):
        # code here
        if M <= 1:
            return 1
        if M == 2:
            return 0
        if M%2 == 0:
            if M%4 == 0:
                return M//2
            return M//2-1
        else:
            if (M-1)%4==0:
                return M//2+1
            return M//2

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        M = int(input())
        
        ob = Solution()
        print(ob.costOfSweets(M))
# } Driver Code Ends