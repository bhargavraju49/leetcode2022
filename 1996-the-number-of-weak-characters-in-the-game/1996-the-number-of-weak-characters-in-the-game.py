class Solution:
    def numberOfWeakCharacters(self, k: List[List[int]]) -> int:
        x = sorted(k, key=lambda x: x[1],reverse=True)
        
        d = defaultdict(list)
        
        for i in x:
            
            d[i[1]].append(i[0])
            
        kys = list(d.keys())
        
        c = max(d[kys[0]])
        res = 0
        for i in kys[1:]:
            tmp = d[i]
            c1 = tmp[0]
            for i in tmp:
                if i<c:
                    res+=1
                if i>c1:
                    c1 = i
            
            c = max(c, c1)
        
        return res
            
            
        