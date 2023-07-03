#User function Template for python3
class Solution:
	def maxIndexDiff(self,arr,n):
		#code here
		l, r, min1, max1 = [arr[0]], [arr[-1]], arr[0], arr[-1]
        for i in range(1, n):
            if arr[i]<min1:min1 = arr[i]
            l.append(min1)
            if arr[n-1-i]>max1:max1 = arr[n-1-i]
            r.append(max1)
        r.reverse()
        i, j, ans = 0, 0, 0
        while i<n and j<n:
            if l[i]<=r[j]:ans, j = max(ans, j-i), j+1
            else:i, j = i+1, j+1
        return ans

#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends