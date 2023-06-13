#User function Template for python3

class Solution:
    def getSmallest(self, N):
        # code here
        if N==1:
            return 1
        r = []
        for i in range(9,1,-1):
            while N%i==0:
                N = N//i
                r.append(str(i))
        if N>10:
            return -1
        return ''.join(r[::-1]) if r else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.getSmallest(N))
# } Driver Code Ends