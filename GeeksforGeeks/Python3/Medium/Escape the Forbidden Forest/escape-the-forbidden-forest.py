class Solution:
    def build_bridges(self, str1, str2):
        # code here
        dp=[[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(str1)][len(str2)]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        obj = Solution()
        str1, str2 = input().split()
        print(obj.build_bridges(str1, str2))

# } Driver Code Ends