#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        # Code here
        A.sort()
        B.sort()
        N = len(A)
        pq = []
        heapq.heapify(pq)
        pq.append((-A[N-1] - B[N-1], (N - 1, N - 1)))
        my_set = set()
        my_set.add((N - 1, N - 1))
        res=[]
        for count in range(K):
            temp = heapq.heappop(pq)
            res.append(-temp[0])
            i = temp[1][0]
            j = temp[1][1]
            sum = A[i - 1] + B[j]
            temp1 = (i - 1, j)
            if(temp1 not in my_set):
                heapq.heappush(pq, (-sum, temp1))
                my_set.add(temp1)
            sum = A[i] + B[j - 1]
            temp1 = (i, j - 1)
            if(temp1 not in my_set):
                heapq.heappush(pq, (-sum, temp1))
                my_set.add(temp1)
        return res


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxCombinations(N, K, A, B)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends