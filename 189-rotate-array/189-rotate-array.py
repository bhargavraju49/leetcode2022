class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k>len(nums):
            k=k%len(nums)
        if len(nums)!=1:
            nums[:]=nums[-k:]+nums[:-k]


        