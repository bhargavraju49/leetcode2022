class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         mi = (k * (k + 1)) // 2
#         ma = 45 - ((9 - k) * (10 - k)) // 2
#         if n == mi:
#             res = []
#             for i in range(1, k + 1):
#                 res.append(i)
#             return [res]

#         elif n == ma:
#             res = []
#             for i in range(9 - k + 1, 10):
#                 res.append(i)
#             return [res]

#         elif n > ma or n < mi:
#             return []

        def combi (k,n,s,l):
            if k == 1 and n>=s and n<10:
                l.append(n)
                Res.append(l)
                return
            elif( k==1 and (n<s or n>9)):
                return

            for i in range(s,10):
                if n-i>=i+1 and combi(k-1,n-i,i+1,l+[i])!=None:
                    pass

        Res = []
        combi(k, n, 1, [])
        return Res