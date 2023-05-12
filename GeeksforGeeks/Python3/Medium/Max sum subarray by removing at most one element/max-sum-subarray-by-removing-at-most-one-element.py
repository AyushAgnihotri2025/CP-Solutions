# Your task is to complete this function



class Solution:
    #Function to return maximum sum subarray by removing at most one element.
    def maxSumSubarray(self, arr, n):
        # Code here
        left = [0] * n
        right = [0] * n
    
        right[-1] = arr[-1]
        left[0] = arr[0]
    
        ans = left[0]
    
        for i in range(1, n):
            left[i] = max(left[i - 1] + arr[i], arr[i])
            ans = max(ans, left[i])
    
            right[n - 1 - i] = max(right[n - i] + arr[n - 1 - i], arr[n - 1 - i])
    
        ans = max(ans, right[1])
    
        for i in range(1, n - 1):
            ans = max(ans, left[i - 1] + right[i + 1])
    
        ans = max(ans, left[n - 2])
    
        return ans


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().maxSumSubarray(arr, n))
# Contributed By: Harshit Sidhwa


# } Driver Code Ends