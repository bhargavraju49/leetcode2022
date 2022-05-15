class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {}
        for i in times:
            if graph.get(i[0]) is None:
                graph[i[0]] = [[i[1], i[2]]]  # dictonary[node] = [[neighnour,distance]]
            else:
                graph[i[0]] += [[i[1], i[2]]]
        dp = [sys.maxsize]*n
        q = [(k,0)]
        visited = []
        while q:
            src,dis= q.pop(0)
            if dis < dp[src-1]:
                dp[src-1] = dis
                if graph.get(src):
                    for target, time in graph[src]:
                        q.append((target, dis + time))
        res = max(dp)
        if res == sys.maxsize:
            return -1
        return res