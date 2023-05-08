class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_sum = secondary_sum = 0
        for i in range(n):
            primary_sum += mat[i][i]
            secondary_sum += mat[i][n - 1 - i]
        return primary_sum + secondary_sum - (mat[n//2][n//2] if n%2 == 1 else 0)