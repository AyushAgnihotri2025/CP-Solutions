
class Solution:
    def distance(self,X, Y):
        # code here
        if X == Y:
            return 0
        d = 0
        while X != Y:
            if X > Y:
                X = X // 2
            else:
                Y = Y // 2
            d += 1
        return d

#{ 
 # Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X,Y = input().split()
        X = int(X)
        Y = int(Y)
        ob = Solution()
        print(ob.distance(X,Y))
# } Driver Code Ends