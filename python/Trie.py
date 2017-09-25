

class TrieNode(object):
    def __init__ (self, value = None, parent = None):
        self.value = value
        self.parent = parent
        self.children = {}
        self.isTerminating = False
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
            if currentIndex == len(word):
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


    # c -> a -> t. -> s. -> d -> o -> g -> c -> a -> t -> s.
    # d -> o -> g. -> c -> a -> t -> s -> d -> o -> g.
    # h -> i -> p -> p -> o -> p -> o -> t -> a -> m -> u -> s -> e -> s.
    # r -> a -> t. -> c -> a -> t -> d -> o -> g -> c -> a -> t.
    def isConcatenated(self, word, numberOfConcat = 0):
        currentNode = self._root
        currentIndex = 0
        #base case
        if not word and numberOfConcat < 2:
            return False
        elif len(word) == 1 and word[0] not in currentNode.children and numberOfConcat < 2:
            return False
        elif not word:
            return True

        if word[0] in currentNode.children:
            currentNode = currentNode.children[word[0]]
        currentIndex = 1
        #find next terminated char
        while currentIndex < len(word):
            char = word[currentIndex]
            if not currentNode.isTerminating and char in currentNode.children:
                currentNode = currentNode.children[char]
                currentIndex += 1
            else:
                break

        # recursive call
        nextWord = word[currentIndex:]

        return self.isConcatenated(nextWord, numberOfConcat + 1)

    def FindLongestConcatenated(self, content):
        currentNode = self._root
        first = ""
        second = ""
        third = ""

        for word in content:
            if self.isConcatenated(word):
                if len(word) >= len(first):
                    third = second
                    second = first
                    first = word
        return [first, second, third]
