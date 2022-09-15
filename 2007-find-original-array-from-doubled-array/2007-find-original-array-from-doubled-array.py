class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        data = Counter(changed)
        result = []
        for k in sorted(data):
            if data[k] < 0:
                return []
            value = k * 2
            while data[k] > 0:
                if value not in data and data[value] == 0 or k == 0 and data[k] < 2:
                    return []
                result.append(k)
                data[k] -= 1
                data[value] -= 1
        return result