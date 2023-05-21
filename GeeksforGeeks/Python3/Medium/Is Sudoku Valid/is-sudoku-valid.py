#User function Template for python3

class Solution:
    def isValid(self, mat):
        # code here
        for i in range(9):
            dicr={}
            dicc={}
            for j in range(9):
                if mat[i][j]!=0:
                    if mat[i][j] in dicr:
                        return 0
                    else:
                        dicr[mat[i][j]]=1
            for k in range(9):
                if mat[k][i]!=0:
                    if mat[k][i] in dicc:
                        return 0
                    else:
                        dicc[mat[k][i]]=1
        r = 0
        c = 0
        for i in range(9):
            if i==3 or i==6 :
                c = 0
                r = i
            else:
                c = 3 * (i%3)
            dup=[]
            for j in range(r,r+3):
                for k in range(c,c+3):
                    if mat[j][k] !=0:
                        if mat[j][k] in dup:
                            return 0
                        else:
                            dup.append(mat[j][k])
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends