
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prev = [-1] * 10001
        curr_sum, max_sum, l = 0, 0, 0
        for r, num in enumerate(nums):
            if prev[num] >= l:
                curr_sum -= sum(nums[l : prev[num] + 1])
                l = prev[num] + 1
            curr_sum += num
            prev[num] = r
            max_sum = max(max_sum, curr_sum)

        return max_sum