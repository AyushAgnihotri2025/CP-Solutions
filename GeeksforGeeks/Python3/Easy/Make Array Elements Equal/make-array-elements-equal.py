#User function Template for python3

class Solution:
    def minOperations(self, N):
        # Code here
        n = ((N-1)//2) + 1
        return n*N - (1+(2*((N-1)//2)+1))*n//2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        ob = Solution()
        print(ob.minOperations(N))
        
        T -= 1

# } Driver Code Ends