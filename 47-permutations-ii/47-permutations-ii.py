class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def helper (nums,k):
            if nums == []:
                if k not in Res:
                    Res.append(k)
                return
            
            for i in nums:
                nums = nums[1:]+[nums[0]]
                helper(nums[1:],k+[nums[0]])

        
        
        Res = []
        helper(nums,[])
        
        return Res
        