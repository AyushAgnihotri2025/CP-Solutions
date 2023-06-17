#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def numberOfSubarrays(self, arr, N, target):
        # Code here
        ans = 0
        currsum = 0
        i,j = 0,0
        hashMap = dict()
        while j < N:
            currsum += arr[j]
            if currsum == target:
                ans += 1
            ans += hashMap.get(currsum-target,0)
            hashMap[currsum] = hashMap.get(currsum,0)+1
            j += 1
        return ans


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, target = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.numberOfSubarrays(arr, N, target)
        print(res)
# } Driver Code Ends