class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list2=[]
        first=-1
        last=-1
        for i in range(0,len(nums)):
            if (nums[i]!=target):
                continue
            if (first==-1):
                first=i
            last=i
        list2.append(first)
        list2.append(last)
        return list2
                
        