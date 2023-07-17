#User function Template for python3

class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		l = []
        m = {}
        ans = ''
        for x in A:
            if x not in m:
                l.append(x)
                m[x]=1
            else:
                if x in l:
                    l.remove(x)
            ans += l[0] if l else '#'
        return ans

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends