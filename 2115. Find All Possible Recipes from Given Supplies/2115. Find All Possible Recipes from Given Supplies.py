class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        indegree_stat = defaultdict(int)

        for index,recipe in enumerate(recipes):
            indegree_stat[recipe]=len(ingredients[index])
            for ingr in ingredients[index]:
                graph[ingr].append(recipe)
                indegree_stat[ingr]=1 if  indegree_stat[ingr] ==0 else  indegree_stat[ingr]

        for supply in supplies:
            indegree_stat[supply]=0

        que = deque()
        for recipe in graph.keys():
            if( indegree_stat[recipe] ==0):
                que.append(recipe)
                
        answer = []
        while(que):
            recipe = que.popleft()
            if(recipe in recipes):
                answer.append(recipe)

            for ingr in graph[recipe]:
                indegree_stat[ingr]-=1 
                if(indegree_stat[ingr]==0):
                    que.append(ingr)
        return answer
