#User function Template for python3

class Solution:
    def toyCount(self, N, K, arr):
        # code here
        ans=0
        count = 0
        arr=sorted(arr)
        for i in arr:
            ans+=i
            if ans<=K:
                count+=1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = [int(x) for x in input().split()]
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        print(ob.toyCount(N, K, arr))
# } Driver Code Ends