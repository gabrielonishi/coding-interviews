"""
The sliding window technique is an algorithm for working
with arrays. It can be used to diminish the time complexity
by avoiding redundant sub-array calculations.

Example problem: Find the maximum sum of sub-array of size
k with the time complexity of O(N).
"""
from typing import List

array = [1, 2, 6, 2, 4, 1]
k = 3

def fixed_window(array: List[int], k: int):
    """
    Complexity of O(N * k)
    """
    max_sum = 0
    for i in range(len(array) - k + 1):
        for j in range(k):
            sub_array = array[i:i + k]
            this_sum = sum(sub_array)
            max_sum = max(max_sum, this_sum)
    
    return max_sum


def sliding_window(array: List[int], k: int):
    """
    Complexity of O(N)
    """
    max_sum = 0
    window_sum = sum(array[:k])
    for i in range(len(array) - k):
        window_sum = window_sum - array[i] + array[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
        
print(fixed_window(array, k))