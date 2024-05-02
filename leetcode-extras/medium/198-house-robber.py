class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [1, 2, 3, 1]
         0  1  2  3
        search(1)
            search(i = 2, total = 1)
                search(i = 4, total = 4)
                search(i = 5, total = 4)
                ret 4
            search(i = 3, total = 1)
                search(i = 5, total = 2)
                search(i = 6, total = 2)
                ret 2
            rete 4

        '''
        memo = dict()

        def search(i: int, total: int = 0) -> int:
            if i >= len(nums):
                return total

            if i in memo:
                return total + memo[i]

            total_one_step = search(i + 2, total + nums[i])
            total_two_step = search(i + 3, total + nums[i])
            max_val = max(total_one_step, total_two_step)
            steps_after = max_val - total
            memo[i] = steps_after

            return max_val

        return max(search(0), search(1))
