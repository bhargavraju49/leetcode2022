class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = dict()
        
        for i in strs:
            ele = sorted(i)
            res[''.join(ele)] = res.get(''.join(ele),[]) + [i]
            
            
        return list(res.values())
            
        