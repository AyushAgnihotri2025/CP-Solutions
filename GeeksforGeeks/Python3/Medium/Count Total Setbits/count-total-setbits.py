#User function Template for python3

class Solution:
    def countBits(self, N):
        # code here
        p=N+1
        i=1
        c=0
        while(i<32):
            c+=(p//(2**i))*(2**(i-1))
            k=p%(2**(i))
            if k-(2**(i-1))>0:
                c+=k-(2**(i-1))
            i+=1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.countBits(N))
# } Driver Code Ends