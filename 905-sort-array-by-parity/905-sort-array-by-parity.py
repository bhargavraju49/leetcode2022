class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if i%2 == 1:
                res.append(i)
            else:
                res = [i]+res
        return res
        