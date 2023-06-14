#User function Template for python3

class Solution:
    def minCost(self, N, cost):
        # code here
        for i in range(1,N):
            cost[i][0] += min(cost[i-1][1],cost[i-1][2])
            cost[i][1] += min(cost[i-1][2],cost[i-1][0])
            cost[i][2] += min(cost[i-1][1],cost[i-1][0])
        return min(cost[-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        cost = [[0]*3 for x in range(N)]
        for i in range(N):
            a = input().split()
            for j in range(3):
                cost[i][j] = int(a[j])
        
        ob = Solution()
        print(ob.minCost(N, cost))
# } Driver Code Ends