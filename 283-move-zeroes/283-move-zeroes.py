
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        for val in nums:
            if val != 0:
                nums[lo] = val
                lo += 1
        for idx in range(lo, len(nums)):
            nums[idx] = 0
        