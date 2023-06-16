#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import heapq

class Solution:
    def replaceWithRank(self, N, arr):
        # Code here
        heap = []
        for i in range(N):
            heapq.heappush(heap,arr[i])
        ans = []
        result = []
        for i in range(N):
            ans.append(heapq.heappop(heap))
        rank = 1    
        d = {}
        for i in range(N):
            if ans[i] not in d:
                d[ans[i]] = rank
                rank += 1
        for i in range(N):
            result.append(d[arr[i]])
        return result


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.replaceWithRank(N, arr)
        for rank in res:
            print(rank, end = ' ')
        print()
# } Driver Code Ends