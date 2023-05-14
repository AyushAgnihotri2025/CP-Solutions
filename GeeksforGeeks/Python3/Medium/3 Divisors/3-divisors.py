#User function Template for python3

from math import sqrt

class Solution:
	def threeDivisors(self, query, q):
		# code here
	    primes = []
        mx = 1000001
        sieve = [True]*mx
        for i in range(2, mx):
            if sieve[i]:
                primes.append(i)
                for j in range(i*i, mx, i):
                    sieve[j]=False
	    l = []
	    for i in query:
	        c=0
	        j = 0
	        while primes[j]*primes[j]<=i:
	            j+=1
	            c+=1
	        l.append(c)
	    return l



#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends