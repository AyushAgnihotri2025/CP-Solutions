#User function Template for python3
import heapq

class Solution:
    def maxDiamonds(self, A, N, K):
        # code here
        A, res = [-1*i for i in A], 0
        heapq.heapify(A)
        for i in range(K):
            temp = -1*heapq.heappop(A)
            res+=temp
            heapq.heappush(A, -1*(temp//2))
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends