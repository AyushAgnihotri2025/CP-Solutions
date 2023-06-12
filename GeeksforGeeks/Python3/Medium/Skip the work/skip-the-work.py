#User function Template for python3

class Solution:
    def minAmount(self, A, n): 
        # code here 
        t1, t2 = A[0], 0
        for i in range(1,n):
            t1, t2 = A[i] + min(t1,t2), t1
        return min(t1,t2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minAmount(A, n))
# } Driver Code Ends