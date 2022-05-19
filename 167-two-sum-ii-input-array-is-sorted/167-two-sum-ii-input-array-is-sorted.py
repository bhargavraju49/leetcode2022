class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0 
        r=len(numbers)-1
        for i in numbers:
            s=numbers[l]+numbers[r]
            if s == target:
                return [l+1,r+1]
            if s > target:
                r=r-1
            else:
                l=l+1