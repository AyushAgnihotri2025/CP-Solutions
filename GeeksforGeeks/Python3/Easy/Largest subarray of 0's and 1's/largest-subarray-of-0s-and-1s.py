#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        # code here
        nums = arr
        psum = {0:0}
        curr_sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
            if curr_sum in psum:
                ans = max(ans,i+1 - psum[curr_sum])
            if curr_sum not in psum:
                psum[curr_sum] = i+1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends