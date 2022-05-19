class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        if k>N:
            k=k%N
        if len(nums)!=1:
            p=nums[-k:]+nums[:-k]
            for i in range(len(nums)):
                nums[i]=p[i]

        