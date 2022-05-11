class Solution:
    def countVowelStrings(self, n: int) -> int:
        N = [1]*5
        sigN = sum(N)
        for i in range(n-1):
            k = [sigN]
            for j in range(1,5):
                k.append(k[j-1] - N[j-1])
            N=k
            sigN = sum(N)
            pass
        return (sigN)
    
#     vowels = ['a', 'e', 'i', 'o', 'u']

#     def helper(v, n, s):
#         if n == 0:
#             Res.append(s)
#             return
#         for i, j in enumerate(v):
#             helper(v[i:], n - 1, s + j)

#     Res = []

#     helper(vowels, n, '')
#     print(Res)
        
