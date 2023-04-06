class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col, visited):
            visited.add((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c] == 0:
                    dfs(grid, r, c, visited)

        count = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0 and (row, col) not in visited:
                    is_closed = True
                    stack = [(row, col)]
                    closed_visited = set()
                    while stack:
                        r, c = stack.pop()
                        if (r, c) in closed_visited:
                            continue
                        closed_visited.add((r, c))
                        if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1:
                            is_closed = False
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                                stack.append((nr, nc))
                                visited.add((nr, nc))
                    if is_closed:
                        count += 1
                        visited.update(closed_visited)
        return count