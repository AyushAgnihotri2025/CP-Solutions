#User function Template for python3

class Solution:
	def AlternatingaMaxLength(self, nums):
		# Code here
        stateMap = [[0 for i in range(2)] for _ in range(len(nums))]
        stateMap[0][0], stateMap[0][1] = 1,1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                stateMap[i][0] = max(stateMap[i-1][1] + 1, stateMap[i-1][0])
                stateMap[i][1] = stateMap[i-1][1]
            elif nums[i] < nums[i-1]:
                stateMap[i][0] = stateMap[i-1][0]
                stateMap[i][1] = max(stateMap[i-1][0] + 1, stateMap[i-1][1])
            else:
                stateMap[i][0] = stateMap[i-1][0]  
                stateMap[i][1] = stateMap[i-1][1]
        return max(stateMap[-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.AlternatingaMaxLength(nums)
		print(ans)

# } Driver Code Ends