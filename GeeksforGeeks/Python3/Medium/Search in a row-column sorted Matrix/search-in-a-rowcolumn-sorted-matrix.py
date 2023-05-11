
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def search(self,matrix, n, m, x): 
    	# code here 
    	
        """
        Function to search a given number in row-column sorted matrix.
        
        Args:
            matrix: A 2D list of integers.
            n: The number of rows in the matrix.
            m: The number of columns in the matrix.
            x: The number to search for.
        
        Returns:
            True if the number is found in the matrix, False otherwise.
        """
        
        i = 0
        j = n - 1
        while i < n and j >= 0:
            if matrix[i][j] == x:
                return True
            elif matrix[i][j] > x:
                j -= 1
            else:
                i += 1
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		size = input().strip().split()
		r = int(size[0])
		c = int(size[1])
		line = input().strip().split()
		matrix = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				matrix[i][j] = int( line[i*c+j] )
		target = int(input())
		obj = Solution()
		if (obj.search(matrix,r,c,target)): 
			print(1) 
		else: 
			print(0) 


# } Driver Code Ends