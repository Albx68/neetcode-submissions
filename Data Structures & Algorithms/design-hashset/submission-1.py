class MyHashSet:

    def __init__(self):
        self.cache = {}

    def add(self, key: int) -> None:
        self.cache[key] = True

    def remove(self, key: int) -> None:
        self.cache[key] = False

    def contains(self, key: int) -> bool:
        return key in self.cache and self.cache[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)