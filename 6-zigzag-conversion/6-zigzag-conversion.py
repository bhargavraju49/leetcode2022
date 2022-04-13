class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1:
            return s
        colsD = n + n - 2
        # gap = n-1
        cols = (n - 1) * (len(s) // colsD)
        if len(s) % colsD > n:
            cols += 1 + ((len(s) % colsD) % n)
        elif len(s) % colsD <= n and len(s) % colsD != 0:
            cols += 1
        ans = [['' for i in range(cols)] for j in range(n)]

        start = 0
        c = 0
        while (c < len(s)):
            for i in range(n):
                ans[i][start] = s[c]
                c += 1
                if c == len(s):
                    break
            start += 1

            if c >= len(s):
                break

            for i in range(n - 2 ,0 ,-1):
                ans[i][start] = s[c]
                c += 1
                start+=1
                if c == len(s):
                    break
        an = ''
        for i in ans:
            for j in i:
                an += j
        return an

            