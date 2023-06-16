from typing import List


from typing import List


class Solution:
    def findShortestPath(self, mat : List[List[int]]) -> int:
        # code here
        rows =  len(mat)
        cols = len(mat[0])
        cant_visit = {}
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    cant_visit[(row, col)] = 1
                    cant_visit[(row-1, col)] = 1
                    cant_visit[(row, col-1)] = 1
                    cant_visit[(row+1, col)] = 1
                    cant_visit[(row, col+1)] = 1
        dist = [[10**6 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            if (row, 0) not in cant_visit:
                self.helper(row, 0, cant_visit, mat, dist)
        ans = 10**6
        for row in range(rows):
            ans = min(ans, dist[row][cols - 1])
        if ans >= 10**6:
            return -1
        return ans

    def helper(self,i, j, cant_visit, mat, dist):
        q = [(i, j, 1)]
        while q:
            (i, j, d) = q.pop(0)
            for (new_i, new_j) in [(i+1,j), (i-1, j), (i, j+1), (i,j-1)]:
                if new_i < 0 or new_j < 0 or new_i >= len(mat) or new_j >= len(mat[0]) or (new_i, new_j) in cant_visit:
                    continue
                if dist[new_i][new_j] > d+1:
                    q.append((new_i, new_j, d+1))
                    dist[new_i][new_j] = d+1

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
        
        
        mat=IntMatrix().Input(a[0], a[1])
        
        obj = Solution()
        res = obj.findShortestPath(mat)
        
        print(res)
        

# } Driver Code Ends