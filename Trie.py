

class TrieNode:
    children = {}
    isTerminating = False
    def __init__ (self, value = None, parent = None):
        self.value = value
        self.parent = parent
    def addChild(self, child):
        if child in self.children:
            return
        self.children[child] = TrieNode(child, None)


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def Insert(self, word):
        if not word:
            return

        currentNode = self._root
        currentIndex = 0

        while currentIndex < len(word):
            char = word[currentIndex]
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                currentNode.addChild(char)
                currentNode = currentNode.children[char]

            currentIndex += 1
        currentNode.isTerminating = True

    def Contains(self, word):
        if not word:
            return

        currentNode = self._root
        currentIndex = 0

        while currentIndex < len(word):
            char = word[currentIndex]
            if char in currentNode.children:
                currentNode = currentNode.children[char]
                currentIndex += 1
                if currentIndex == len(word) and currentNode.isTerminating:
                    return True

        return False
