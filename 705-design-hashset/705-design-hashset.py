class MyHashSet:
    def __init__(self):
        self.set = {}

    def add(self, key: int) -> None:
        self.set[key] = ""

    def remove(self, key: int) -> None:
        if key in self.set.keys():
            del self.set[key]

    def contains(self, key: int) -> bool:
        if key in self.set.keys():
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)