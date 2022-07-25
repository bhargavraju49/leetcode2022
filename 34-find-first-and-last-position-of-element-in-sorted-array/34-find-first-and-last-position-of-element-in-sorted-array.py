class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        start = 0
        end = len(nums)-1
        
        while start<=end:
            mid = (start+end)//2
            if nums[mid]>target:
                end = mid-1
            elif nums[mid]<target:
                start = mid+1
            elif nums[mid]==target:
                k = mid
                
                while k < len(nums)  and k > -1 and nums[k] == target:
                    k -= 1
                res[0] = k + 1

                while k+1 < len(nums) and nums[k + 1] == target  :
                    k += 1
                res[1] = k
                return res
        return res
                
        