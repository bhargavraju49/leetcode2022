class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev=nums[0]
        curr = 0
        for i in nums:
            curr=curr+i
            if prev < curr:
                prev=curr
            if curr<0:
                curr=0
        return prev