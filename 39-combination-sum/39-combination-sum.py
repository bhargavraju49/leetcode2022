class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        #sorting before calling
        
        def result(nums , target):
            res = []                                        
            for i in nums:
                if i == target:         # every entry go from here if fails [] returns always such that entry wont takes place 
                    res.append([i])    #storing solo grouping and return after first call to add them with another new target
            
            for i in range(len(nums)):
                v = nums[i]
                
                if v>target//2:         # at this point no use of checking further as all are greater than what we need
                    break
                    
                else:
                    res2 = result(nums[i:],target-v)  # calling with same index ensures taking repetetion in call stacks
                    for k in res2:
                        res.append([v] + k)  # adding them in array format 
            
            return res
        
        return result(nums,target)
