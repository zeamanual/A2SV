class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        parent = {(i,j):(i,j) for j in range(len(grid[0])) for i in range(len(grid))}
        
        def is_valid(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        rank = defaultdict(lambda : 1)
        def get_rep(node):
            if(parent[node]!=node):
                parent[node]=get_rep(parent[node])
            return parent[node]

        def union(node1,node2):

            rep1 = get_rep(node1)
            rep2 = get_rep(node2)
            if(rep1!=rep2):
                if(rank[rep1]>rank[rep2]):
                    parent[rep2]=rep1
                elif(rank[rep1]<rank[rep2]):
                    parent[rep1]=rep2
                else:
                    parent[rep2]=rep1
                    rank[rep1]+=1

        def dfs(cord):

            nonlocal visited,curr,counter
            visited.add(cord)

            union(curr,cord)
            counter+=1
            for move in [(0,1),(1,0),(-1,0),(0,-1)]:
                new_row,new_col = cord[0]+move[0],cord[1]+move[1]
                if(
                is_valid(new_row,new_col) and 
                (new_row,new_col) not in visited and
                grid[new_row][new_col]==1
                ):
                    dfs((new_row,new_col))

        visited = set()
        component_size = defaultdict(lambda : 0)
        answer = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr = (row,col)
                counter = 0
                if(curr not in visited and grid[curr[0]][curr[1]]==1):
                    dfs(curr)
                    component_size[get_rep(curr)]=counter
                    answer=max(answer,component_size[get_rep(curr)])

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if(grid[row][col]==0):   
                    curr,curr_linked,curr_answer = (row,col),set(),1
                    for move in [(0,1),(1,0),(-1,0),(0,-1)]:
                        new_row,new_col = row+move[0],col+move[1]  
                        if(is_valid(new_row,new_col) and grid[new_row][new_col]==1 and get_rep((new_row,new_col)) not in curr_linked):
                            curr_answer+=component_size[get_rep((new_row,new_col))]
                            curr_linked.add(get_rep((new_row,new_col)))

                    answer=max(answer,curr_answer)

        return answer
