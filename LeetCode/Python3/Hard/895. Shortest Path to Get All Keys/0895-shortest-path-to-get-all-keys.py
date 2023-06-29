class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m , n =len(grid) , len(grid[0])
        keys = 0
        sr,sc=None,None
        for i in range(m):
            for j in range(n):
                if 97<=ord(grid[i][j])<=122:keys+=1
                if grid[i][j] == '@':sr,sc=i,j
        d = ""
        if 97<=ord(grid[sr][sc])<=122:d= grid[sr][sc]
        queue =[(sr,sc,0,d)]
        dp = {(sr,sc,d):True}
        while queue:
            row , col , dis , key = queue.pop(0)
            if len(key) == keys:return dis
            # Try to move in four directions
            new = ((row+1,col),(row-1,col),(row,col-1),(row,col+1))
            for r,c in new:
                if 0<=r<m and 0<=c<n and grid[r][c]!='#':
                    if 65<=ord(grid[r][c])<=90:
                        # its a lock
                        k = grid[r][c].lower()
                        #print(k,key)
                        if k in key and (r,c,key) not in dp:
                            queue.append((r,c,dis+1,key))
                            dp[(r,c,key)]=True
                    elif 97<=ord(grid[r][c])<=122:
                        # its a key
                        new = key+grid[r][c] if grid[r][c] not in key else key
                        new = "".join(sorted(list(new)))
                        if (r,c,new)  in dp:continue
                        queue.append((r,c,dis+1,new))
                        dp[(r,c,new)] = True
                    else:
                        if (r,c,key) in dp:continue
                        queue.append((r,c,dis+1,key))
                        dp[(r,c,key)]  = True     
        return -1