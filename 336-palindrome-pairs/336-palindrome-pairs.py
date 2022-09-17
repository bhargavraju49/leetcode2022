class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        rmap = {w[::-1]:i for i,w in enumerate(words)}
        res = []
        for i,w in enumerate(words):
            if w in rmap:
                if rmap[w] != i:
                    res.append([i,rmap[w]])
            for j in range(1,len(w)+1):
                if w[:-j] in rmap and w[-j:] == w[-j:][::-1]:
                        res.append([i,rmap[w[:-j]]])
                if w[j:] in rmap and w[:j] == w[:j][::-1]:
                    res.append([rmap[w[j:]],i])
        return res