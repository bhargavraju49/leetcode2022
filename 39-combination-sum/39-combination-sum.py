class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        self.targetSum = 0
        
        def backtrack(nums, start, track):
            
            for i in range(start,len(nums)):
                if self.targetSum == target:
                    res.append(track.copy())
                    return

                if self.targetSum > target:
                    return

                track.append(nums[i])
                self.targetSum += nums[i]
                backtrack(nums, i, track) 
                
                self.targetSum -= track.pop()
        
        backtrack(candidates, 0, track)
        return res