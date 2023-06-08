#User function Template for python3

class Solution:
    def coinsGame (self, N, K):
        # code here
        ans,temp = [],[]
        result = [0] * K
        for i in range(2,K,2):
            result[i] = 1
        result[0] = N - sum(result)
        ans.append(result)
        for i in ans:
            for j in i:
                temp.append(int(j))
        temp.append("")
        return temp

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N, K= map(int, input().split())
        ans = ob.coinsGame(N,K);
        print(*ans)


# } Driver Code Ends