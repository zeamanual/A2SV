"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = dict()

        for employee in employees:
            graph[employee.id]=[employee.importance,employee.subordinates]

        importance = 0
        def dfs(node):
            nonlocal importance
            importance += graph[node][0]
            for nbr in graph[node][1]:
                    if(not visited[nbr]):
                        visited[nbr]=True
                        dfs(nbr)

        visited = [False for i in range(2001)]

        dfs(id)

        return importance
