#User function Template for python3

class Solution:
    def computeBeforeMatrix(self, N, M, after):
        # Code here
        before = [[0 for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if i==0:
                    if j>0:
                        before[i][j] = after[i][j]-after[i][j-1]
                    else:
                        before[i][j] = after[i][j]
                elif i>0:
                    if j==0:
                        before[i][j] = after[i][j]-after[i-1][j]
                    else:
                        before[i][j] = after[i][j]-((after[i][j-1]-after[i-1][j-1])+after[i-1][j])
        return before

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, M =[int(i) for i in input().split()]
        after= []
        for j in range (N):
            after.append([int(i) for i in input().split()])
        ob = Solution()
        before=ob.computeBeforeMatrix(N,M,after)
        for i in range(len(before)): 
            for j in range(len(before[i])):
                print(before[i][j],end=' ')
            print()
        
        
        T -= 1
# } Driver Code Ends