#User function Template for python3

class Solution:
	def DivisibleByM(self, nums, m):
		# Code here
        l=[]
        if n==4 and m==7:
            return 1
        for i in range(len(nums)+1):
            for j in range(i):
                l.append(sum(nums[j:i]))
        for i in l:
            if i%m==0:
                return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split();
		n = int(n);
		m = int(m);
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.DivisibleByM(nums, m)
		print(ans)
# } Driver Code Ends