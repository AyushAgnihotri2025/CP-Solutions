#User function Template for python3
class Solution: 
    def countStrings(self, N): 
        # Code here
        mod=10**9+7
        def matrix_multiplication(mat1,mat2,mod):
            matrix=[[0,0],[0,0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        matrix[i][j]=(matrix[i][j]+mat1[i][k]*mat2[k][j])%mod
            return matrix
        def power_m(mat,N,mod):
            if N==1:
                return mat
            else:
                sq=power_m(mat,N//2,mod)
                res=matrix_multiplication(sq,sq,mod)
            if N%2!=0:
                res=matrix_multiplication(res,mat,mod)
            return res
        mat=[[1,1],[1,0]]
        return power_m(mat,N+1,mod)[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        
        ob = Solution()
        print(ob.countStrings(int(input())))
        
        T -= 1
# } Driver Code Ends