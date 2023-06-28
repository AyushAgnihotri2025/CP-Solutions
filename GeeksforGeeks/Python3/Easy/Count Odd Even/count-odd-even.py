#User function Template for python3

class Solution:
	def countOddEven(self, arr, n):
		#Code here
		OddCount, EvenCount = 0, 0
        for i in range(len(arr)):
            if(arr[i]%2 ==0):
                EvenCount= EvenCount+1
            else:
                OddCount= OddCount+1
        out= str(OddCount)+" "+str(EvenCount)     
        return(print(out))  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
    	obj = Solution()
    	obj.countOddEven(arr, n);
# } Driver Code Ends