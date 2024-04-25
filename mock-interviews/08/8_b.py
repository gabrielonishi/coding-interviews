"""
Question 16.19 - Cracking the Coding Interview
Pond Sizes

You have an integer matrix representing a plot of land, where the value at that 
location represents the height above sea level. A value of zero indicates water. 
A pond is a region of water connected vertically, horizontally, or diagonally. The 
size of the pond is the total number of connected water cells. Write a method to 
compute the sizes of all ponds in the matrix.

Examples

Input:

     0 1 2 3 x
   
  0  0 2 1 0
  1  0 1 0 1
  2  1 1 0 1
  3  0 1 0 1
  y
  
Output: 2, 4, 1 (in any order)
"""


def compute_pond_sizes(land: list[list[int]]) -> list[int]:
    x_length = len(land[0])
    y_length = len(land)

    visited = set()
    ponds = list()

    def check_neighbors(x: int, y: int, pond_size: int) -> int:
        # right limit
        has_right = x + 1 < x_length
        has_left = x - 1 >= 0
        has_up = y - 1 >= 0
        has_down = y + 1 < y_length
        # à direita
        if has_right and land[y][x + 1] == 0 and (x + 1, y) not in visited:
            visited.add((x + 1, y))
            pond_size += 1
            pond_size = check_neighbors(x+1, y, pond_size)
        # abaixo
        if has_down and land[y + 1][x] == 0 and (x, y + 1) not in visited:
            visited.add((x, y+1))
            pond_size += 1
            pond_size = check_neighbors(x, y+1, pond_size)
        # diagonal direita abaixo
        if has_right and has_down and land[y+1][x+1] == 0 and (x + 1, y + 1) not in visited:
            visited.add((x+1, y+1))
            pond_size += 1
            pond_size = check_neighbors(x+1, y+1, pond_size)
        # diagonal esquerda abaixo
        if has_left and has_down and land[y+1][x-1] == 0 and (x - 1, y + 1) not in visited:
            visited.add((x-1, y+1))
            pond_size += 1
            pond_size = check_neighbors(x-1, y+1, pond_size)
        # esquerda
        if has_left and land[y][x-1] == 0 and (x - 1, y) not in visited:
            visited.add((x-1, y))
            pond_size += 1
            pond_size = check_neighbors(x-1, y, pond_size)
        # acima
        if has_up and land[y - 1][x] == 0 and (x, y - 1) not in visited:
            visited.add((x, y-1))
            pond_size += 1
            pond_size = check_neighbors(x, y - 1, pond_size)
        # diagonal direita acima
        if has_right and has_up and land[y-1][x+1] == 0 and (x + 1, y - 1) not in visited:
            visited.add((x+1, y-1))
            pond_size += 1
            pond_size = check_neighbors(x+1, y-1, pond_size)
        # diagonal esquerda acima
        if has_left and has_up and land[y-1][x-1] == 0 and (x - 1, y - 1) not in visited:
            visited.add((x-1, y-1))
            pond_size += 1
            pond_size = check_neighbors(x-1, y-1, pond_size)
        return pond_size

    for y in range(y_length):
        for x in range(x_length):
            if land[y][x] == 0 and (x, y) not in visited:
                pond_size = 1
                visited.add((x, y))
                pond_size = check_neighbors(x, y, pond_size)
                ponds.append(pond_size)

    return ponds
