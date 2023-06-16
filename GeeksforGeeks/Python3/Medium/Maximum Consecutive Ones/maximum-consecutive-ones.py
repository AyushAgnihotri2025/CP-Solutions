#User function Template for python3

class Solution:
    def longestOnes(self, n, a, k):
        # Code here
        ans=-1
        j=0
        cnt=k
        for i in range(n):
            if a[i]==0 and cnt==0:
                while cnt==0 and j<i:
                    if a[j]==0:
                        cnt+=1
                    j+=1
            if a[i]==0:
                cnt-=1
            ans=max(ans,(i-j)+1)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        print(ob.longestOnes(n, a, k))
# } Driver Code Ends