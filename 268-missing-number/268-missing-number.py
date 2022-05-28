class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _len = len(nums)
        _len = (_len*(_len+1))//2
        return _len-sum(nums)