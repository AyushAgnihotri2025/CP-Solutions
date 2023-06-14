#User function Template for python3

class Solution:    
    def ValidCorner(self,matrix): 
        # Your code goes here
        d={}
        n=len(matrix)
        m=len(matrix[0])
        for h in range(n):
            d[h]=set()
            for g in range(m):
                if matrix[h][g]==1:
                    d[h].add(g)
            for y in range(h-1,-1,-1):
                if len(d[h].intersection(d[y]))>=2:
                    return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		r = int(input())
		c = int(input())
		line = input().strip().split()
		mat = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				mat[i][j] = int( line[i*c+j] )
		ob=Solution()
		if (ob.ValidCorner(mat)): 
			print("Yes") 
		else: 
			print("No") 


# } Driver Code Ends