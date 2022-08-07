class Solution:
    def countVowelPermutation(self, n: int) -> int:
        graph = {
            "$":"aeiou",
            "a":"e",
            "e":"ai",
            "i":"aeou",
            "o":"iu",
            "u":"a",
        }
        memo = {(c,0):1 for c in "aeiou"}
        M = 10**9+7
        def dfs(x, n):
            if (x,n) not in memo:
                memo[x,n] = sum(dfs(y, n-1) for y in graph[x]) % M
            return memo[x,n]
        return dfs("$", n)
        
        