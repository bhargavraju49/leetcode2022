class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSum_sorted(candidates, target)
        
    def combinationSum_sorted(self, candidates, target):
        res=[]
        if target in candidates:
            res.append([target])
        
        for i in range(len(candidates)):
            v = candidates[i]
            if v > target//2:
                break
            else:
                res_next = self.combinationSum_sorted(candidates[i:], target-v)
                for res1 in res_next:
                    res.append([v] + res1)
        return res