class Solution:
    def canJump(self, nums: List[int]) -> bool:
        quota = 1
        for i,num in enumerate(nums[:-1]):
            quota -= 1
            if num > quota:
                quota = num
            if quota == 0:
                return False
        return True