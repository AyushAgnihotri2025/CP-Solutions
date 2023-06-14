#User function Template for python3

class Solution:
    def diagonalSort(self, matrix, n, m):
        # code here
        lft=[]
        up=[]
        dg=[]
        for i in range(1,n):
            st=i
            en=0
            ans=[]
            while(0<=en<m and 0<=st<n):
                ans.append(matrix[st][en])
                en+=1
                st+=1
            ans.sort()
            st=i
            en=0
            while(0<=en<m and 0<=st<n and ans):
                matrix[st][en]=ans.pop(0)
                en+=1
                st+=1
        for i in range(1,m):
            st=0
            en=i
            ans=[]
            while(0<=en<m and 0<=st<n):
                ans.append(matrix[st][en])
                en+=1
                st+=1
            ans.sort(reverse=True)
            st=0
            en=i
            while(0<=en<m and 0<=st<n and ans):
                matrix[st][en]=ans.pop(0)
                en+=1
                st+=1
        return matrix

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        inputLine = list(map(int, input().strip().split()))
        matrix = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                matrix[i][j] = inputLine[i * m + j]
        ob=Solution()
        ob.diagonalSort(matrix,n,m)
        for i in range(n): 
            for j in range(m): 
                print(matrix[i][j], end =' ') 
            print() 
        tc-=1

# } Driver Code Ends