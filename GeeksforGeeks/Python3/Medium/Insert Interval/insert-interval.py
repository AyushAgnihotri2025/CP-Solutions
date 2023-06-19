#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def insertNewEvent(self, N, intervals, newEvent):
        # Code here
        intervals.append(newEvent)
        intervals.sort(key=lambda i:i[0])
        res = [intervals[0]]
        for x1, y1 in intervals[1:]:
            x, y = res[-1]
            if x1<=y:res[-1][1]=max(y, y1)
            else:res.append([x1, y1])
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertNewEvent(N, intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
# } Driver Code Ends