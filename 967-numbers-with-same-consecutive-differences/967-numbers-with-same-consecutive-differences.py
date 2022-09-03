class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        res = []

        def helper(i, k, n, s):
            if n == 1:
                res.append(s)
                # print(s)
                return

            if i + k < 10:
                helper(i + k, k, n - 1, s + str(i + k))
            if i - k >= 0:
                helper(i - k, k, n - 1, s + str(i - k))

            return

        for i in range(1, 10):
            helper(i, k, n, str(i))

        return list(set(res))
            
            
                
            
        