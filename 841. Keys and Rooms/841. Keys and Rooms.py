class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        def dfs(room):
            nonlocal visited 
            visited.add(room)
            for nbr in rooms[room]:
                if(nbr not in visited):
                    dfs(nbr)

        dfs(0)

        return len(visited)==len(rooms)
