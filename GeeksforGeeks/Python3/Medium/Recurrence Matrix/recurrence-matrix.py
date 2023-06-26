#User function Template for python3

class Solution:
	def CountOnes(self, Queries):
		# Code here
        A = [1,0,1,0,0,1,1]
        B, count = [0]*1001, 0
        for i in range(1, 1001):
            x = i*i*i
            count += A[x*x%7]
            for j in range(1, i):
                count += A[x*j*j*j%7] * 2
            B[i] = count
        res = []
        for q in Queries:
            res.append(B[q])
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		Queries = []
		for _ in range(q):
		    Queries.append(int(input()))
		obj = Solution()
		ans = obj.CountOnes(Queries)
		for _ in ans:
			print(_)

# } Driver Code Ends