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

    print(land[1][0])

    visited = set()
    ponds = list()

    def check_neighbors(x: int, y: int, pond_size: int) -> int:
        # à direita
        if x + 1 < x_length and land[y][x + 1] == 0 and (x + 1, y) not in visited:
            visited.add((x + 1, y))
            pond_size += 1
            pond_size = check_neighbors(x+1, y, pond_size)
        # abaixo
        if y + 1 < y_length and land[y + 1][x] == 0 and (x, y + 1) not in visited:
            visited.add((x, y+1))
            pond_size += 1
            pond_size = check_neighbors(x, y+1, pond_size)
        # diagonal direita
        if x + 1 < x_length and y + 1 < y_length and land[y+1][x+1] == 0 and (x + 1, y + 1) not in visited:
            visited.add((x+1, y+1))
            pond_size += 1
            pond_size = check_neighbors(x+1, y+1, pond_size)
        # diagonal esquerda
        if x - 1 > 0 and y + 1 < y_length and land[y+1][x-1] == 0 and (x - 1, y + 1) not in visited:
            visited.add((x-1, y+1))
            pond_size += 1
            pond_size = check_neighbors(x-1, y+1, pond_size)
        return pond_size

    for y in range(y_length):
        for x in range(x_length):
            if land[y][x] == 0 and (x, y) not in visited:
                pond_size = 1
                visited.add((x, y))
                pond_size = check_neighbors(x, y, pond_size)
                ponds.append(pond_size)

    return ponds
