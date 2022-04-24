class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        
        
        def result(nums , target):
            res = []
            for i in nums:
                if i == target:
                    res.append([i])
            
            for i in range(len(nums)):
                v = nums[i]
                
                if v>target//2:
                    break
                    
                else:
                    res2 = result(nums[i:],target-v)
                    for k in res2:
                        res.append([v] + k)
            
            return res
        
        return result(nums,target)
