#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
        m = arr[0]
        m2 = -1
        for i in range(1, n):
            if arr[i] > m:
                m2 = m
                m = arr[i]
            elif arr[i] < m and arr[i] > m2:
                m2 = arr[i]
        return m2

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends