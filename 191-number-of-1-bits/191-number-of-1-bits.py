class Solution:
    def hammingWeight(self, n: int) -> int:
        print(bin(n))
        return bin(n).count('1')
        