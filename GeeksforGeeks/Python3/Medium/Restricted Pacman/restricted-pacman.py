#User function Template for python3

class Solution: 
    def candies(self, m,n): 
        # Your code goes here
        maxi = m*n
        setti = set()
        for i in range(m+1):
            for j in range(n+1):
                num = i*n + j*m
                if num < maxi:
                    setti.add(num)
        return maxi - len(setti) 

#{ 
 # Driver Code Starts
#Initial Template for Python 3
	
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
    	arr = list(map(int, input().strip().split()))
    	m = arr[0]
    	n = arr[1]
    	obj = Solution()
    	print(obj.candies(m,n)) 



# } Driver Code Ends