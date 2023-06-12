class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, columns = len(dungeon), len(dungeon[0])
        hp = [[0]*columns for i in range(rows)]
        hp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in range(rows-2, -1,-1):
            hp[i][-1] = max(1, hp[i+1][-1] - dungeon[i][-1])  
        for j in range(columns-2, -1, -1): 
            hp[-1][j] = max(1, hp[-1][j+1] - dungeon[-1][j])
        for i in range(rows-2, -1, -1):
            for j in range(columns-2, -1, -1):                
                hp[i][j] = max(1, min(hp[i+1][j] - dungeon[i][j], hp[i][j+1] - dungeon[i][j]) )
        return hp[0][0]