from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # TC: O(NlogN)
        res = []
        sorted_nums = SortedList(nums)
        # print(sorted_nums)
        for num in nums:
            res.append(sorted_nums.index(num))
            sorted_nums.remove(num)
            # print(sorted_nums)

        
        return res