class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        result, solution = Solution.helper(arr, start, visited)
        return result

    def helper(arr: List[int], start: int, visited: set) -> bool:
        if start in visited:
            return False, visited

        visited.add(start)

        if start >= len(arr) or start < 0:
            return False, visited

        if arr[start] == 0:
            return True, visited

        result_plus, visited = Solution.helper(
            arr, start + arr[start], visited)
        result_minus, visited = Solution.helper(
            arr, start - arr[start], visited)

        return result_plus or result_minus, visited
