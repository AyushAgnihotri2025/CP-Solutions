#User function Template for python3

class Solution:
    def geekNumber(self, N):
        # code here
        if N in [1,2,3] :
            return 1
        k = int(N**0.5 + 0.5)
        for i in range(2 , k + 1) :
            if N % i == 0 :
                if N % (i ** 2) == 0 :
                    return 0
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        if ob.geekNumber(N)==1 :
            print("Yes");
        else :
            print("No");
# } Driver Code Ends