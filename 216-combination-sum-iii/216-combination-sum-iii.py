class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def combi (k,n,s,l):
            if k == 1 and n>=s and n<10:
                Res.append(l+[n])
                return
            elif( k==1 and (n<s or n>9)):
                return

            for i in range(s,10):
                if n-i>=i+1 and combi(k-1,n-i,i+1,l+[i])!=None:
                    pass

        Res = []
        combi(k, n, 1, [])
        return Res