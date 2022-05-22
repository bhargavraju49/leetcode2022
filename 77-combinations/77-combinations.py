class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res =[]
        def helper(n,k,r = []):
            if len(n)<k:
                return
            if k == 0:
                res.append(r)
                return
            for i in range(len(n)):
                helper(n[i+1:],k-1,r+[n[i]])
        
        helper([i for i in range(1,n+1)],k)
        return res