class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for fr, to in roads:
            graph[fr].append(to)
            graph[to].append(fr)

        ans = 0 
        for i in range(n):
            curr_max1 = len(graph[i])
            for j in range(i+1,n):
                curr_max2 = len(graph[j])
                reduce_by = 1 if (j in graph[i]) else 0
                cur_ans = curr_max1 + curr_max2 - reduce_by
                ans = max(ans,cur_ans)

        return ans 
