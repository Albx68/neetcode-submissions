class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)

        if endWord not in wordset:
            return 0
        
        queue = deque([(beginWord,1)])
        visited = set([beginWord])

        while queue:
            word,level = queue.popleft()
            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    newword = word[:i] + letter + word[i+1:]
                    if newword in wordset and newword not in visited and newword != word:
                        if newword == endWord:
                            return level+1
                        queue.append((newword,level+1))
                        visited.add(newword)
        return 0