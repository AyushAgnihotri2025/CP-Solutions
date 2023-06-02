#User function Template for python
class Solution:
    def findElement(self, a, n, x, ranges, k):
        # code here
        for i in reversed(range(k)):
            if x == ranges[i][0]:
                x = ranges[i][1]
            elif x > ranges[i][0] and x <= ranges[i][1]:
                x -= 1
        return a[x]

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ranges = [[0 for i in range(2)] for j in range(k)]

        inputLine = list(map(int, input().strip().split()))
        kt=0
        for i in range(k):
            for j in range(2):
                ranges[i][j] = inputLine[kt]
                kt+=1

        ans = Solution().findElement(arr, n, x, ranges, k)
        print(ans)
        tc -= 1

# } Driver Code Ends