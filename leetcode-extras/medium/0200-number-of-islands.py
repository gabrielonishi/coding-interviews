from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        x_length = len(grid[0])
        y_length = len(grid)

        visited = set()

        def explore_neighbor(x: int, y: int) -> None:
            has_right = x + 1 < x_length
            has_left = x - 1 >= 0
            has_up = y - 1 >= 0
            has_down = y + 1 < y_length

            if has_right and grid[y][x+1] == "1" and (x + 1, y) not in visited:
                visited.add((x + 1, y))
                explore_neighbor(x + 1, y)
            if has_left and grid[y][x-1] == "1" and (x - 1, y) not in visited:
                visited.add((x - 1, y))
                explore_neighbor(x - 1, y)
            if has_up and grid[y-1][x] == "1" and (x, y - 1) not in visited:
                visited.add((x, y - 1))
                explore_neighbor(x, y - 1)
            if has_down and grid[y + 1][x] == "1" and (x, y + 1) not in visited:
                visited.add((x, y + 1))
                explore_neighbor(x, y + 1)

        for y in range(y_length):
            for x in range(x_length):
                if grid[y][x] == '1' and (x, y) not in visited:
                    counter += 1
                    visited.add((x, y))
                    explore_neighbor(x, y)

        return counter
