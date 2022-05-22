class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums,n,r=[]):
            if n==0:
                res.append(r)
                return
            for i in range(n):
                nums = nums[1:]+[nums[0]]
                helper(nums[1:],n-1,r+[nums[0]])
                
            pass
        
        helper(nums,len(nums))
        
        return res
        