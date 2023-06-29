class Solution:
    def findSum(self, A, N): 
        #code here
        max = A[0]
        for i in range(N):
            if A[i] > max:
                max = A[i]
        min = A[0]
        for i in range(N):
            if A[i] < min:
                min = A[i]
        return max + min

#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends