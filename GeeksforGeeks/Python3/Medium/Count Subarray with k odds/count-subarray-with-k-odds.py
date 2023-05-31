#User function Template for python3

class Solution:
    def countSubarray(self, n, nums, k):
        # Code here
        l = 0
        r = 0
        d = {}
        total_c = 0
        d = {0:0}
        count = 0
        for i in range(n):
            nums[i] = nums[i]%2
        while r<n:
            count += nums[r]
            if count == k:
                total_c += 1
            if count-k in d:
                total_c += d[count-k]
            d[count] = d.get(count,0) + 1
            r+= 1
        return total_c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        print(ob.countSubarray(n, nums, k))
# } Driver Code Ends