#User function Template for python3

class Solution:
    #Function to find minimum number of operations that are required 
    #to make the matrix beautiful.
    def findMinOpeartion(self, matrix, n):
        # code here
        ts = 0
        hs = 0
        for i in range(n):
            cr = 0
            for j in range(n):
                ts +=matrix[i][j]
                cr +=matrix[i][j]
            cc = 0
            for j in range(n):
                cc +=matrix[j][i]
            hs = max(cc,cr,hs)
        return (n*hs)-ts

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        print(obj.findMinOpeartion(matrix,n))



# } Driver Code Ends