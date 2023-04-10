class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indgree_status = defaultdict(int)

        for fr,to in edges:
            indgree_status[to]+=1
            indgree_status[fr] = indgree_status[fr] 

        ans = []
        for node in indgree_status.keys():
            if(indgree_status[node]==0):
                ans.append(node)

        return ans
