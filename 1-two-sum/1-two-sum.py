class Solution(object):
    def twoSum(self, nums, target):
        k=[]
        for i in nums:
            k.append(i)
        print(k)
        s=0
        e=len(nums)-1
        nums.sort()
        for i in range(len(nums)):
            if (nums[s]+nums[e]==target):
                if nums[e]!=nums[s]:
                    return [k.index(nums[s]),k.index(nums[e])]
                else:
                    a=k.index(nums[s])
                    k[a]='x'
                    b=k.index(nums[s])
                    return(a,b)
            elif (nums[s]+nums[e]>target):
                e=e-1
            else:
                s=s+1
                
