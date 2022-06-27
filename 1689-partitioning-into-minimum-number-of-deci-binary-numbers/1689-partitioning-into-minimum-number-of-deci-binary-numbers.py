class Solution:
    def minPartitions(self, n: str) -> int:
        k = int(n[0])
        for i in n:
            k = max(k, int(i))
        return k
        