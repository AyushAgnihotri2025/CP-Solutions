#User function Template for python3
class Solution:
	def NBitBinary(self, N):
		# code here
        opList=[]
        def nbitRec(ones,zeros,n,op):
            if n==0:
                opList.append(op)
                return
            nbitRec(ones+1,zeros,n-1,op+"1")
            if ones>zeros:
                nbitRec(ones,zeros+1,n-1,op+"0")
        nbitRec(0,0,N,"")
        return opList

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends