#User function Template for python3

import heapq

class Solution:    
    def minimumPlatform2(self, arr, dep, days, platforms):
        a = []
        n = len(arr)
        for i in range(n):
            a.append((arr[i], dep[i], days[i]))
        a.sort(key = lambda x : (x[2], x[0], x[1]))
        need = 0
        day = -1
        pq = []
        for i in range(n):
            if a[i][2] > day:
                pq = []
                day = a[i][2]
            while len(pq) > 0 and pq[0] <= a[i][0]:
                heapq.heappop(pq)
            heapq.heappush(pq, a[i][1])
            need = max(need, len(pq))
        return need <= platforms

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        days = list(map(int, input().strip().split()))
        platforms = int(input())
        ob=Solution()
        print(ob.minimumPlatform2(arrival, departure, days, platforms))
# } Driver Code Ends