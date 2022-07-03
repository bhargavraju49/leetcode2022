class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 0
        rest = nums[0]
        incflag = False
        decflag = False
        for i in nums[1:]:
            if i>rest and not incflag:
                rest = i
                count+=1
                incflag = True
                decflag = False
            elif i<rest and not decflag:
                rest = i
                count+=1
                incflag = False
                decflag = True
            else:
                rest = i
        return count+1
                
            
        