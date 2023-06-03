#User function Template for python3

class Solution:
    def distributeCandies(self, N, K):
        # code here
        result = [0]*K
        i = 0
        while N > 0:
            candy = min(N,i+1)
            result[i%K] += candy
            N -= candy
            i +=1
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        
        ob = Solution()
        res = ob.distributeCandies(N,K)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends