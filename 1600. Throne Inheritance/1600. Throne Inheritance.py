class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph=defaultdict(list)
        self.kingName = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        return self.dfs(self.kingName,[])
    
    def dfs(self,curr,curr_order):
        if(curr not in self.dead):
            curr_order.append(curr)

        for child in self.graph[curr]:
            self.dfs(child,curr_order)

        return curr_order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
