#User function Template for python3

class Solution:
	def bitonic(self, arr, n):
		# code here
        if (n==0):
            return 0
        maxLen = 1
        start = 0
        nextStart = 0
        j = 0
        while (j < (n-1)):
            while (j < n-1) and (arr[j] <= arr[j+1]):
                j += 1
            while (j < n-1) and (arr[j] >= arr[j+1]):
                if (j < n-1) and (arr[j] > arr[j+1]):
                    nextStart = j+1
                j += 1
            maxLen = max(maxLen, j-(start-1))
            start = nextStart
        return maxLen

#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.bitonic(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends