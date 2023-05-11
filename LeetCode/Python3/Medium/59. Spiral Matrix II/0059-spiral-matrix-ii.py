class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize the matrix with zeros
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        # Initialize the boundaries
        top, bottom, left, right = 0, n-1, 0, n-1
        
        # Initialize the direction and the count
        direction, count = 0, 1
        
        while top <= bottom and left <= right:
            if direction == 0:  # Traverse from left to right
                for i in range(left, right+1):
                    matrix[top][i] = count
                    count += 1
                top += 1
            elif direction == 1:  # Traverse from top to bottom
                for i in range(top, bottom+1):
                    matrix[i][right] = count
                    count += 1
                right -= 1
            elif direction == 2:  # Traverse from right to left
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = count
                    count += 1
                bottom -= 1
            elif direction == 3:  # Traverse from bottom to top
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = count
                    count += 1
                left += 1
            
            # Update the direction
            direction = (direction + 1) % 4
            
        return matrix