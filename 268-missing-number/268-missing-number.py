class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        _len = (len(nums)*(len(nums)+1))//2
        return _len-sum(nums)