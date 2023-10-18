class RandomizedSet:

    def __init__(self):
        self.store=set()
        

    def insert(self, val: int) -> bool:
        if(val in self.store):
            return False
        self.store.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if(val in self.store):
            self.store.discard(val)
            return True

        return False
        

    def getRandom(self) -> int:
        return random.sample(self.store, 1)[0]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
