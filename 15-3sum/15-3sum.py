class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if len(nums) == 3 and sum(nums)!=0:
            return[]
        nums.sort()
        res = []
        
        for i in range (len(nums)-2):
            target = -nums[i]
            start = i+1
            end = len(nums)-1
            
            while start < end:
                if nums[start] + nums[end] == target:
                    if [nums[i],nums[start],nums[end]] not in res:
                        res.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                elif nums[start] + nums[end] > target:
                    end-=1
                else:
                    start+=1
        
        return res
                    