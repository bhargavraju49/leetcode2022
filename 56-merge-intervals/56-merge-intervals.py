class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        res = []
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                k = [intervals[i][0] ,max(intervals[i+1][1],intervals[i][1])]
                intervals[i+1] = k
            else:
                res.append(intervals[i])
        if not res:
            return [k]
        if intervals[-1][1] == res[-1][1]:
            return res
        
        return res + [intervals[-1]]
                