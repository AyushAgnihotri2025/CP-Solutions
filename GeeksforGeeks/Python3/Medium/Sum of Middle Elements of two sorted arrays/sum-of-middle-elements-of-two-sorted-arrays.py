#User function Template for python3

class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here
        ans = []
        for i in range(n):
            ans.append(ar1[i])
            ans.append(ar2[i])

        # Sort the list
        ans.sort()

        # Return the sum of the two middle elements
        return ans[(2 * n) // 2 - 1] + ans[2 * n // 2]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends