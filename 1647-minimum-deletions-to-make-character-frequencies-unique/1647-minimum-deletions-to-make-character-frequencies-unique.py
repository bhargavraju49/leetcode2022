class Solution:
    def minDeletions(self, s: str) -> int:

        cnt = Counter(s)
        seen = set()

        res = 0
        for v in cnt.values():
            while v in seen and v > 0:
                v -= 1; res += 1
            seen.add(v)

        return res