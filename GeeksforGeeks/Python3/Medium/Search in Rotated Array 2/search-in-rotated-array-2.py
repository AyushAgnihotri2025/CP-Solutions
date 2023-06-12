#User function Template for python3

class Solution:
    def Search(self, n, arr, k):
        # code here
        return 0 if k not in arr else 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        ans = ob.Search(n, arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends