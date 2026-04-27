class PrefixTree:

    def __init__(self):
        self.strings = []

    def insert(self, word: str) -> None:
        self.strings.append(word)

    def search(self, word: str) -> bool:
        if word in self.strings:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for s in self.strings:
            if prefix in s:
                return True
        return False
        