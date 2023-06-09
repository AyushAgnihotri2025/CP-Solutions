#User function Template for python3

class Solution:
    def querySum(self, n, arr, q, queries):
        # code here
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        ans = []
        for j in range(q):
            ans.append(prefix[queries[2*j+1]] - prefix[queries[j*2]-1])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        q = int(input())
        queries = input().split()
        for i in range(0,2*q,2):
            queries[i] = int(queries[i])
            queries[i+1] = int(queries[i+1])
        
        ob = Solution()
        ans = ob.querySum(n, arr, q, queries)
        for it in(ans):
            print(it,end=" ")
        print()
# } Driver Code Ends