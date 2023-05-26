class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowVal, R, C =1,  len(matrix), len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i != 0:       
                        matrix[i][0] = 0
                    else:
                        firstRowVal = 0
        for i in reversed(range(R)):
            for j in reversed(range(C)):
                if i == 0:
                    matrix[i][j] *= firstRowVal
                elif matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0