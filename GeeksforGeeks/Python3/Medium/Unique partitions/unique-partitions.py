#User function Template for python3

class Solution:
    def util(self,a,n,S,s):
        global ans
        if S==0:
            s=s[:-1]
            s=s.split(',')
            ans.append(s)
            return
        if n==0:
            return
        if a[n-1]<=S:
            self.util(a,n,S-a[n-1],s+str(a[n-1])+",")
            self.util(a,n-1,S,s)
        else:
            self.util(a,n-1,S,s)
        
    def UniquePartitions(self, n):
        # Code here
        global ans
        ans=[]
        a=[i for i in range(1,n+1)]
        self.util(a,n,n,'')
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.UniquePartitions(n)
		for a in ans:
			for b in a:
				print(b, end = " ")
		print()

# } Driver Code Ends