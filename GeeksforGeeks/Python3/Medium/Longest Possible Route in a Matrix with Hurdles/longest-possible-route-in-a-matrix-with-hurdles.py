from typing import List

class Solution:
    def longestPath(self,mat : List[List[int]],n : int, m : int, xs : int, ys : int, xd : int, yd : int) -> int:
        # code here
        if mat[xs][ys]==0:
            return -1
        if mat[xd][yd]==0:
            return -1
        count=0
        ans=[]
        string='udlr'
        di=[-1,1,0,0]
        dj=[0,0,-1,1]
        def path(i,j,ds,visited):
            if i==xd and j==yd:
                ans.append(len(ds))
                return
            for k in range(len(string)):
                if (i+di[k]>=0 and j+dj[k]>=0) and (i+di[k]<n and j+dj[k]<m) and mat[i+di[k]][j+dj[k]]==1 and  not visited[i+di[k]][j+dj[k]]:
                    visited[i][j]=1
                    path(i+di[k],j+dj[k],ds+string[k],visited)
                    visited[i][j]=0
        visited=[]
        for i in range(n):
            visited.append([0]*m)
        path(xs,ys,'',visited)
        if ans==[]:
            return -1
        return max(ans)

#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        b=IntArray().Input(4)
        
        
        mat=IntMatrix().Input(a[0], a[0])
        
        obj = Solution()
        res = obj.longestPath(mat,a[0],a[1],b[0],b[1],b[2],b[3])
        
        print(res)
        


# } Driver Code Ends