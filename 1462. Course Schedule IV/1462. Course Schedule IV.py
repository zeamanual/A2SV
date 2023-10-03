class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        adj_mat = [[float('inf') for i in range(n)] for j in range(n)]
        
        for pre in prerequisites:
            adj_mat[pre[0]][pre[1]]=1
        

        for i in range(n):
            adj_mat[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj_mat[i][j]= min(adj_mat[i][j], adj_mat[i][k] + adj_mat[k][j])

        answer = []
        for query in queries:
            if(adj_mat[query[0]][query[1]]==float('inf')):
                answer.append(False)
            else:
                answer.append(True)

        return answer
