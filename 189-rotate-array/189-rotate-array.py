class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while(k>len(nums)):
            k=k-len(nums)
        if len(nums)!=1:
            p=nums[-k:]+nums[:-k]
            for i in range(len(nums)):
                nums[i]=p[i]

        