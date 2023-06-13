#User function Template for python3

class Solution:
    def numOfPairs(self, X, Y, N):
        # code here
        ans = 0
        xMap = {}
        yMap  = {}
        xyMap  = {}
        for i in range(N):
            x = X[i]
            y = Y[i]
            xValue = xMap.get(x, 0)
            yValue = yMap.get(y, 0)
            comb = str(x) + "*" + str(y)
            xyValue =  xyMap.get(comb, 0)
            ans += (xValue + yValue - 2*xyValue)
            xMap[x] = xValue + 1
            yMap[y] = yValue + 1
            xyMap[comb] = xyValue + 1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        X=list(map(int,input().split()))
        Y=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.numOfPairs(X,Y,N))
# } Driver Code Ends