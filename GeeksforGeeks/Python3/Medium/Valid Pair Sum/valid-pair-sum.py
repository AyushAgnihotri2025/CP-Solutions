#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def ValidPair(self, a, n): 
    	# Your code goes here
        a.sort()
        i=0
        while a[i]<0:
            i+=1
        j=i
        t=n-j
        i-=1
        ans=0
        while i>=0 and j<n:
            if a[i]+a[j]<0:
                j+=1
            elif a[i]+a[j]>0:
                i-=1
                ans+=(n-j)
            else:
                j+=1
        ans+=(t*(t-1))//2
        return ans

#{ 
 # Driver Code Starts.

if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		n = int(input())
		array = list(map(int, input().strip().split()))
		obj = Solution()
		ans = obj.ValidPair(array, n)
		print(ans) 



# } Driver Code Ends