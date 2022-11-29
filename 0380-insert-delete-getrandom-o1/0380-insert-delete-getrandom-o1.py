class RandomizedSet:

    def __init__(self):
        self.set_ = set()
        # self.val = val

    def insert(self, val: int) -> bool:
        if val not in self.set_: 
            self.set_.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set_: 
            self.set_.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.sample(self.set_,1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()