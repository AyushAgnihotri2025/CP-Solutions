#User function Template for python3
class Solution:
	def maxCalories(self, Arr, n):
		# code here
		ans=[]
        if(n<=2):
            return sum(Arr)
        ans.append(Arr[0])
        ans.append(Arr[1]+Arr[0])
        ans.append(max(ans[1],Arr[2]+Arr[0],Arr[1]+Arr[2]))
        for i in range(3,n):
            ans.append(max(Arr[i]+ans[i-2],Arr[i]+Arr[i-1]+ans[i-3],ans[i-1]))
        return ans[n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxCalories(Arr,n)
		print(ans)

# } Driver Code Ends