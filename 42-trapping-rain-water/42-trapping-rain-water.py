class Solution:
    def trap(self, nums: List[int]) -> int:
        def helper(left,right,res,nums):
            cleft = 0
            while left < right:
                if left>=len(nums):
                    break
                k = nums[left]
                if nums[left + 1] >= nums[left]:
                    cleft = left
                    left += 1
                else:
                    cleft = left
                    shift = 0
                    oc = 0
                    left += 1

                    while nums[left] < k:
                        oc += nums[left]
                        left += 1
                        shift += 1
                        if left >= len(nums):
                            break
                    if left<len(nums):
                        res += k * shift - oc
                        cleft = left
            # print(left, nums[left-1], res,cleft)
            return cleft,res

        left = 0
        right = len(nums) - 1
        res = 0

        newl,lres = helper(left,right,res,nums)
        # print(newl,lres)
        if newl < len(nums)-1:
            rnums = nums[newl:][::-1]
            new2l,rres = helper(0,len(rnums)-1,0,rnums)
            return rres+lres
        else:
            return lres
                