#User function Template for python3

class Solution:
    def minSum(self, a, n):
        # Write your code here
        if n <= 2:
            return 0
        dp = [0] * n
        dp[0] = a[0]
        dp[1] = a[1]
        dp[2] = a[2]
        for i in range(3, n):
            dp[i] = a[i] + min(dp[i - 1], dp[i - 2], dp[i - 3])
        return min(dp[n - 1], dp[n - 2], dp[n - 3])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()






# } Driver Code Ends