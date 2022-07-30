class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        for i, j in enumerate(words1):
            k = {}
            k["value"] = j
            for l in j:
                k[l] = k.get(l, 0) + 1

            words1[i] = k

        for i, j in enumerate(words2):
            k = {}

            for l in j:
                k[l] = k.get(l, 0) + 1

            words2[i] = k

        jdict = {}

        for i in words2:
            for j in i:
                if jdict.get(j,0)<i.get(j):
                    jdict[j] = i[j]

        for k, j in enumerate(words1):
            if j["value"]=="":
                continue
            for l in jdict:
                if jdict.get(l) > j.get(l,-1):
                    j["value"]=""
                    break

        res = []
        for i in words1:
            if i.get("value")=='':
                continue
            else:
                res.append(i.get("value"))
        return res
