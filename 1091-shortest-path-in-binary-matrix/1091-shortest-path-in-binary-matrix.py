class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Determine if grid is valid
        if not grid or rows == 0 or cols == 0 or grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        shortest_path_length = 0
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        queue = deque()
        queue.append([0, 0])
        visited[0][0] = True

        while queue:
            queue_size = len(queue)
            shortest_path_length += 1

            for i in range(queue_size):
                current_cell = queue.popleft()

                # Check if current cell is goal state
                if current_cell[0] == rows - 1 and current_cell[1] == cols - 1:
                    return shortest_path_length

                for direction in directions:
                    next_cell = [sum(x) for x in zip(current_cell, direction)]
                    x_val, y_val = next_cell
                    # Validate next cell is in grid and not yet visited
                    if x_val < 0 or y_val < 0 or x_val >= rows or \
                            y_val >= cols or visited[x_val][y_val] or grid[x_val][y_val] == 1:
                        continue
                    visited[x_val][y_val] = True
                    queue.append(next_cell)

        return -1  
        
        
        