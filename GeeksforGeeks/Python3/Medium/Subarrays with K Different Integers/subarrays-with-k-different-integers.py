#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def subarraysWithAtmostKDistinct(self, nums,k):
        if k == 0:
            return 0
        count = 0
        freq_map = {}
        l = 0
        for r, elem in enumerate(nums):
            freq_map[elem] = 1 + freq_map.get(elem,0)
            if len(freq_map) > k:
                while len(freq_map) != k:
                    freq_map[nums[l]] -= 1
                    if freq_map[nums[l]] == 0:
                        del freq_map[nums[l]]
                    l += 1
            count += r-l+1
        return count

    def subarrayCount(self, nums, N, k):
        # Code here
        return self.subarraysWithAtmostKDistinct(nums,k) - self.subarraysWithAtmostKDistinct(nums,k-1)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.subarrayCount(arr, N, k)
        print(res)
# } Driver Code Ends