#User function Template for python3

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        # code here
        s=[]
        for i in range(q):
            p=queries[i][0]
            r=queries[i][1]
            c=queries[i][2]
            ans=0
            if(p==1):
                row=r-1
                col=c-1
                if(row>=0):
                    ans=ans+mat[row][c]
                if(col>=0):
                    ans=ans+mat[r][col]
                if(row>=0 and col>=0):
                    ans=ans+mat[row][col]
                row=r+1
                col=c+1
                if(row<n):
                    ans=ans+mat[row][c]
                if(col<m):
                    ans=ans+mat[r][col]
                if(row<n and col<m):
                    ans=ans+mat[row][col]
                row=r+1
                col=c-1
                if(row<n and col>=0):
                    ans=ans+mat[row][col]
                row=r-1
                col=c+1
                if(row>=0 and col<m):
                    ans=ans+mat[row][col]
                s.append(ans)
            else:
                row=r-2
                col=c-2
                if(row>=0):
                    ans=ans+mat[row][c]
                    if c-1 >=0 :
                        ans=ans+mat[row][c-1]
                    if c+1 <m :
                        ans=ans+mat[row][c+1]
                if(col>=0):
                    ans=ans+mat[r][col]
                    if r-1 >=0 :
                        ans=ans+mat[r-1][col]
                    if r+1 <n :
                        ans=ans+mat[r+1][col]
                if(row>=0 and col>=0):
                    ans=ans+mat[row][col]
                row=r+2
                col=c+2
                if(row<n):
                    ans=ans+mat[row][c]
                    if c-1 >=0 :
                        ans=ans+mat[row][c-1]
                    if c+1 <m :
                        ans=ans+mat[row][c+1]
                if(col<m):
                    ans=ans+mat[r][col]
                    if r-1 >=0 :
                        ans=ans+mat[r-1][col]
                    if r+1 <n :
                        ans=ans+mat[r+1][col]
                if(row<n and col<m):
                    ans=ans+mat[row][col]
                row=r+2
                col=c-2
                if(row<n and col>=0):
                    ans=ans+mat[row][col]
                row=r-2
                col=c+2
                if(row>=0 and col<m):
                    ans=ans+mat[row][col]
                s.append(ans)
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        for i in range(n):
            arr = input().split()
            for j in range(m):
                mat[i][j] = int(arr[j])
        q = int(input())
        queries = [[0]*3 for x in range(q)]
        for i in range(q):
            a = input().split()
            for j in range(3):
                queries[i][j] = int(a[j])
        
        ob = Solution()
        ans = ob.matrixSum(n, m, mat, q, queries)
        for i in range(q):
            print(ans[i])
# } Driver Code Ends