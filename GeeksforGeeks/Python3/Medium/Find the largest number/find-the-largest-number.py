#User function Template for python3

#Back-end complete function Template for Python 3

class Solution:
    def find (self, N):
        # code here
        for i in range(N,1,-1):
            n = str(i)
            a = [j for j in n]
            a.sort()
            b = ''.join(a)
            if int(b) == i:
                return i

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))
# } Driver Code Ends