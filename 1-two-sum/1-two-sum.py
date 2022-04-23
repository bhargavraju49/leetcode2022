class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = [i for i in nums]
        nums.sort();
        start = 0
        end = len(nums) - 1
        
        while start < end:
            if nums[start]+nums[end] == target:
                if nums[end]!=nums[start]:
                    return [k.index(nums[start]),k.index(nums[end])]
                else:
                    a=k.index(nums[start])
                    k[a]='x'
                    b=k.index(nums[start])
                    return(a,b)
            elif nums[start]+nums[end] > target:
                end-=1
            elif nums[start]+nums[end] < target:
                start+=1