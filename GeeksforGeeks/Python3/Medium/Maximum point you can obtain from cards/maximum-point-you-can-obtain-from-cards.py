#{ 
 # Driver Code Starts
#Initial Template for Python 3



# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxScore(self, cardPoints, N, k):
        # Code here
        s=0
        for i in range(k):
            s+=cardPoints[i]
        r=s
        z=0
        for i in range(k-1,-1,-1):
            s=s-cardPoints[i]
            s+=cardPoints[N-z-1]
            z+=1
            r=max(r,s)
        return r

#{ 
 # Driver Code Starts.


if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, k = map(int, input().split())
        cardPoints = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxScore(cardPoints, N, k)
        print(res)
# } Driver Code Ends