#User function Template for python3
class Solution:
	def factorial(self,a, n):
    	# code here
        m=10**9+7
        ans=[]
        maxi=max(a)
        fact=[1,1]
        f=1
        for i in range(2,maxi+1):
            f*=i
            f%=m
            fact.append(f)
        for i in a:
            ans.append(fact[i])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        a=list(map(int , input().strip().split()))
        ob = Solution()
        res = ob.factorial(a, n)
        for i in res:
            print(i,end=" ")
        print()
        tc=tc-1
# } Driver Code Ends