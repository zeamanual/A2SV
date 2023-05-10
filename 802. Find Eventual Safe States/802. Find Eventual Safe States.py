class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_ls = defaultdict(list)
        out_degree = [ 0 for i in range(len(graph)) ]

        for index, nbrs in enumerate(graph):
            out_degree[index]=len(nbrs)
            for node in nbrs:
                adj_ls[node].append(index)

        que = deque()
        for node in range(len(graph)):
            if(out_degree[node]==0):
                que.append(node)

        answer = []
        while(que):
            curr = que.popleft()
            answer.append(curr)
            for rnbr in adj_ls[curr]:
                out_degree[rnbr]-=1
                if(out_degree[rnbr]==0):
                    que.append(rnbr)
        answer.sort()
        return answer
