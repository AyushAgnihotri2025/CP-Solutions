#User function Template for python3
MAX = 101
dp = [[[[-1] * 4 for i in range(MAX)] for j in range(MAX)] for k in range(MAX)];
def countWayss(p, q, r, last):
    if (p < 0 or q < 0 or r < 0):
        return 0;
    if (p == 1 and q == 0 and
        r == 0 and last == 0):
        return 1;
    if (p == 0 and q == 1 and
        r == 0 and last == 1):
        return 1;
    if (p == 0 and q == 0 and
        r == 1 and last == 2):
        return 1;
    if (dp[p][q][r][last] != -1):
        return dp[p][q][r][last];
    if (last == 0):
        dp[p][q][r][last] = (countWayss(p - 1, q, r, 1) + countWayss(p - 1, q, r, 2));
    elif (last == 1):
        dp[p][q][r][last] = (countWayss(p, q - 1, r, 0) + countWayss(p, q - 1, r, 2));
    else:
        dp[p][q][r][last] = (countWayss(p, q, r - 1, 0) + countWayss(p, q, r - 1, 1));
    return dp[p][q][r][last];
def countUtil(p, q, r):
    return (countWayss(p, q, r, 0) +
            countWayss(p, q, r, 1) +
            countWayss(p, q, r, 2));
class Solution:
    def CountWays(self, p, q, r):
        # Code here
        return countUtil(p,q,r)%(int(1e9+7))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		p, q, r = map(int,input().split())
		p = int(p); q = int(q); r = int(r);
		ob = Solution()
		ans = ob.CountWays(p, q, r)
		print(ans)
# } Driver Code Ends