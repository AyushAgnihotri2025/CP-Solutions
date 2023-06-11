#User function template for Python

class Solution:
	def longestCommonSum(self, arr1, arr2, n): 
		# code here 
		arr = [0]*n
        for i in range(n):
            arr[i] = arr1[i] - arr2[i]
        d = {0:-1}
        c_sum = 0
        ans = 0
        for i in range(n):
            c_sum += arr[i]
            if c_sum in d:
                ans = max(ans,i-d[c_sum])
            else:
                d[c_sum] = i
        return ans


#{ 
 # Driver Code Starts
#Initial template for Python

def convertToBool(arr):
	a=[]
	for x in arr:
		if x == '1':
			a.append(True)
		else:
			a.append(False)
	return a

# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr1=input().strip().split()
        arr2=input().strip().split()
        arr1=convertToBool(arr1)
        arr2=convertToBool(arr2)
        ob = Solution()
        ans= ob.longestCommonSum(arr1, arr2, n)
        print(ans)
        tc=tc-1
# } Driver Code Ends