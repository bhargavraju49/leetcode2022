class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def helper(nums, k):
            if nums == []:
                Res.append(k)
                return
            visited = []
            for i in (nums):
                nums.append(nums[0])
                nums.pop(0)
                if nums[0] not in visited:
                    visited.append(nums[0])
                    helper(nums[1:], k + [nums[0]])

        Res = []
        helper(nums, [])
        return Res
        