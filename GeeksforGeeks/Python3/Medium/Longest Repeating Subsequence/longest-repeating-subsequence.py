#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		# Code here
        n = len(str)
        str = '.' + str
        prev = [0] * (n+1)
        curr = [0] * (n+1)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if str[i] == str[j] and i != j:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr.copy()
        return curr[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends