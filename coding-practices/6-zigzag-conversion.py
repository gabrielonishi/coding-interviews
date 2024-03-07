'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows

Exemplo: 

s = "PAYPALISHIRING"
len(position) = 14
numRows = 3

char = A
current_y = -1
current_x = 2
position = 4

     0  1  2  3
0  [[P, *, A]
1   [A, P]
2   [Y]]
 
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) == 0 or numRows == 1: return s
        
        matrix = [[] for j in range(numRows)]
        current_y = 0
        current_x = 0
        
        position = 0
        
        while position < len(s):
            if current_y < numRows:
                if len(matrix[current_y]) == current_x:
                    matrix[current_y].append(s[position])
                    current_y += 1
                    position += 1
                else:
                    matrix[current_y].append(None)
            else:
                current_y -= 2
                current_x += 1
                while current_y >= 0 and position < len(s):
                    if len(matrix[current_y]) == current_x:
                        matrix[current_y].append(s[position])
                        current_y -= 1
                        current_x += 1
                        position += 1
                    else:
                        matrix[current_y].append(None)
                current_y += 2
                current_x -= 1
        
        return_s = ''
        
        for line in matrix:
            for element in line:
                if element is not None:
                    return_s += element
        
        return return_s